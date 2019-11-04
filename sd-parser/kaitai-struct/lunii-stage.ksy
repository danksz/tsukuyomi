meta:
  id: luniistage
  file-extension: lunii
  endian: be
instances:
  story_nodes:
    type: node_struct
#    pos: 0x4400
    pos: 0x30D4400
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
