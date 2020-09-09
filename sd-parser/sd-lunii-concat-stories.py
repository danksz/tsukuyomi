#!/usr/bin/env python3

import logging
from lunii import Lunii
import sys
import os
import errno
import shutil

base_file = sys.argv[1]
stories_dir = sys.argv[2]
out_dir = "out/"
dest_file = out_dir + os.path.basename(base_file) + "-mod" + ".img"

logging.basicConfig(filename='dump.log',
                    filemode='w',
                    level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

lun = Lunii.from_file(base_file)
logging.info('Number of stories: {}'.format(lun.contents.nbr_stories))
nbr_stories = lun.contents.nbr_stories
fileoffset = lun.fileoffset

field_sep = '    '
root_sep ='\n'

origin_stories = []

for story in lun.contents.stories:
    story_sep = field_sep
    string  = root_sep  + 'Story[{:02}]\n'.format(lun.contents.stories.index(story))
    string += story_sep + 'address:   0x{:08X}\n'.format(story.abs_start_address)
    string += story_sep + 'size:      0x{:08X}\n'.format(story.size*0x200)
    string += story_sep + 'sector:    0x{:08X}\n'.format(story.start_address)
    string += story_sep + 'nbr_nodes: {:03}'.format(story.story_info.nbr_nodes)
    logging.info(string)
    origin_stories.append((story.abs_start_address, story.size*0x200))

lun.close()
added_stories = origin_stories

try:
    os.makedirs(out_dir)
except OSError as e:
    if e.errno == errno.EEXIST: pass

print("Copy base image to " + dest_file)
shutil.copy2(base_file, dest_file)

with open(dest_file, "r+b") as bfile:
    p, s = origin_stories[-1] #Get the last position size in order to start writing at that position
    destpos = p + s
    for storyfile in os.listdir(stories_dir):
        with open(stories_dir + "/" + storyfile, "rb") as sfile:
            print("Adding {} at 0x{:08X}".format(storyfile,destpos))
            story_data = sfile.read()
            story_size = len(story_data)
            bfile.seek(destpos)
            bfile.write(story_data)
            added_stories.append((destpos, story_size))
            destpos += story_size
            nbr_stories += 1
            # be sure to not exceed available room in the content sector:
            if nbr_stories > ((0x200 - 2)/(3*4)):
                print("maximum number of stories is reached!! skipping the remaining stories!!")

    nbr_stories_bin = nbr_stories.to_bytes(2, byteorder='big',signed=False)

    stories_struct_bin = b""

    for pos, size in added_stories:
        pos    -= fileoffset
        pos   //= 0x200
        size  //= 0x200
        unknown = 0
        pos_bin     = pos.to_bytes(4, byteorder='big',signed=False)
        size_bin    = size.to_bytes(4, byteorder='big',signed=False)
        unknown_bin = unknown.to_bytes(4, byteorder='big',signed=False)
        stories_struct_bin += pos_bin + size_bin + unknown_bin

    content_bin = nbr_stories_bin + stories_struct_bin
    bfile.seek(fileoffset)
    bfile.write(content_bin)
