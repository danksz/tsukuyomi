meta:
  id: lunii
  file-extension: lunii
  endian: be
instances:
  contents:
    type: content_struct
#   pos: 0x4000
    pos: 0x30D4000
types:
  content_struct:
    seq:
      - id: nbr_stories
        type: u2
      - id: stories
        type: stories_location_struct
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