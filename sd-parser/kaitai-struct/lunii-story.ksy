meta:
  id: luniistory
  file-extension: lunii
  endian: be
instances:
  story:
    type: story_struct
#    pos: 0x4200
     pos: 0x30D4200
types:
  story_struct:
    seq:
      - id: nbr_nodes
        type: u2
      - id: factory_disabled
        type: u1
      - id: version
        type: u2
