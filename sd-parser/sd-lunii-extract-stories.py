#!/usr/bin/env python3

import logging
from lunii import Lunii
import sys
import os
import errno

base_file = sys.argv[1]

logging.basicConfig(filename='dump.log',
                    filemode='w',
                    level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

lun = Lunii.from_file(base_file)
logging.info('Number of stories: {}'.format(lun.contents.nbr_stories))

field_sep = '    '
root_sep ='\n'

stories = []

for story in lun.contents.stories:
    story_sep = field_sep
    string  = root_sep  + 'Story[{:02}]\n'.format(lun.contents.stories.index(story))
    string += story_sep + 'address:   0x{:08X}\n'.format(story.abs_start_address)
    string += story_sep + 'size:      0x{:08X}\n'.format(story.size*0x200)
    string += story_sep + 'sector:    0x{:08X}\n'.format(story.start_address)
    string += story_sep + 'nbr_nodes: {:03}'.format(story.story_info.nbr_nodes)
    logging.info(string)
    stories.append((story.abs_start_address, story.size*0x200))

lun.close()

#print(stories)

out_dir = "out-extract/"

with open(base_file, "rb") as bfile:
    i = 0
    try:
        os.makedirs(out_dir)
    except OSError as e:
        if e.errno == errno.EEXIST: pass
    for pos, size in stories:
        dest_file = out_dir + os.path.splitext(os.path.basename(base_file))[0] + "-story" + str(i) + ".lunii"
        print("Extracting story n:{} to {}".format(i, dest_file))
        bfile.seek(pos)
        story_data = bfile.read(size)
        with open(dest_file, "wb") as out_file:
            out_file.write(story_data)
        i += 1
