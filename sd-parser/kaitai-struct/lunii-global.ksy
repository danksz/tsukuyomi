meta:
  id: lunii
  file-extension: lunii
  endian: be
instances:
  contents:
    type: content_struct
#    pos: 0x4000
    pos: 0x30D4000
types:
  content_struct:
    seq:
      - id: nbr_stories
        type: u2
      - id: stories
        type: story_struct
        repeat: expr
        repeat-expr: nbr_stories
  stories_location_struct:
     seq:
      - id: start_address
        type: u4                                                              
      - id: size
        type: u4
      - id: unknown
        type: u4
  story_info_struct:
    seq:
      - id: nbr_nodes
        type: u2
      - id: factory_disabled
        type: u1
      - id: version
        type: u2
  story_struct:
    seq:
      - id: story_locations
        type: stories_location_struct
    instances:
      story_info:
        type: story_info_struct
        #pos: 0x4000 + (story_locations.start_address) * 0x200
        pos: 0x30D4000 + ((story_locations.start_address) * 0x200)
