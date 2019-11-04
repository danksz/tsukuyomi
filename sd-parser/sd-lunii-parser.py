#!/usr/bin/env python3

import logging
from Lunii import Lunii
import sys

logging.basicConfig(filename='dump.log',
                    filemode='w',
                    level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

lun = Lunii.from_file(sys.argv[1])
logging.info('Number of stories: {}'.format(lun.contents.nbr_stories))
for story in lun.contents.stories:
    logging.info('Story n:{:02} start at sector: 0x{:08x} with size: 0x{:08x}'
                 .format(lun.contents.stories.index(story),
                         story.start_address, story.size))
