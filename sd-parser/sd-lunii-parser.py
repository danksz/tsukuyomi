#!/usr/bin/env python3

import logging
from lunii import Lunii
import sys

logging.basicConfig(filename='dump.log',
                    filemode='w',
                    level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

lun = Lunii.from_file(sys.argv[1])
logging.info('Number of stories: {}'.format(lun.contents.nbr_stories))

field_sep = '    '
root_sep ='\n'

for story in lun.contents.stories:
    story_sep = field_sep
    string  = root_sep  + 'Story[{:02}]\n'.format(lun.contents.stories.index(story))
    string += story_sep + 'address:   0x{:08X}\n'.format(story.abs_start_address)
    string += story_sep + 'sector:    0x{:08X}\n'.format(story.start_address)
    string += story_sep + 'size:      0x{:08X}\n'.format(story.size*0x200)
    string += story_sep + 'nbr_nodes: {:03}'.format(story.story_info.nbr_nodes)
    logging.info(string)

    for node in story.story_info.nodes:
        node_sep = story_sep + story_sep
        comp_sep = node_sep + story_sep

        string  = story_sep + 'node[{:03}]\n'.format(story.story_info.nodes.index(node))

        string += node_sep + 'audio\n'
        string += comp_sep + 'addr:   0x{:08X}\n'.format(node.audio_start_address)
        string += comp_sep + 'size:   {}\n'.format(node.audio_size*0x200)
        string += comp_sep + 'object: {}\n'.format(node.audio)

        string += node_sep  + 'image\n'
        string += comp_sep + 'addr:   0x{:X}\n'.format(node.image_start_address)
        string += comp_sep + 'size:   {}\n'.format(node.image_size*0x200)
        string += comp_sep + 'object: {}\n'.format(node.image)

        logging.info(string)
