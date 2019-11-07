meta:
  id: lunii
  file-extension: lunii
  endian: be
instances:
  contents:
    type: content_struct
    pos: 0x30D4000
enums:
  lbool:
    0xffff: disabled
    0x0001: enabled
types:
  node_struct:
    seq:
      - id: uuid
        size: 16
      - id: image_start_sector
        type: u4
      - id: image_size
        type: u4
      - id: audio_start_sector
        type: u4
      - id: audio_size
        type: u4
#If the action is set but the chosen index is -1, then a random option of the list is selected.
      - id: action_on_ok
        type: u2
      - id: option_in_transition
        type: u2
      - id: chosen_option
        type: u2
      - id: wheel_enabled
        type: u2
        enum: lbool
      - id: ok_enabled
        type: u2
        enum: lbool
    #If HOME button is enabled but no action is set (i.e. all transition fields are -1), the user is directed all the way back to the main stage (story-pack selection).
      - id: home_enabled
        type: u2
        enum: lbool
      - id: paused_enabled
        type: u2
        enum: lbool
      - id: autojump_at_audio_ends_enabled
        type: u2
        enum: lbool
    instances:
      images:
        type: bmp
        pos: 0x30D4000 + ((image_start_sector) * 0x200)
        size: image_size * 0x200
        repeat: expr
        repeat-expr: eos
      audios:
        type: wav
        pos: 0x30D4000 + ((audio_start_sector) * 0x200)
        size: audio_size * 0x200
        repeat: expr
        repeat-expr: eos

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
      - id: nodes_info
        type: nodes_struct
        size: 0x200
      - id: nodes
        type: node_struct
        size: 0x200
        repeat: expr
        repeat-expr: nodes_info.nbr_nodes
  nodes_struct:
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
        pos: 0x30D4000 + ((story_locations.start_address) * 0x200)
