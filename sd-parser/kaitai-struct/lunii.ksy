meta:
  id: lunii
  file-extension: lunii
  endian: be
  imports:
    - bmp
    - wav
seq:
   - id: header
     size: fileoffset
   - id: contents
     type: content_struct
instances:
   fileoffset:
     value: 0x30D4000
enums:
  lbool:
    0xffff: disabled
    0x0001: enabled
types:
  navigation_struct:
    seq:
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
      - id: navigation
        type: navigation_struct
        size: 0x200 - 32
    instances:
##### this is just for debugging
      story_start_address:
        value: _parent._parent.abs_start_address
      image_start_address:
        value: story_start_address + ((1 + image_start_sector) * 0x200)
      audio_start_address:
        value: story_start_address + ((1 + audio_start_sector) * 0x200)
#####
      image:
        type: bmp
        pos: image_start_address
        size: image_size * 0x200
        if: image_size != 0xffffffff
      audio:
        type: wav
        pos: audio_start_address
        size: audio_size * 0x200
        if: audio_size != 0xffffffff
      image_raw:
        pos: image_start_address
        size: image_size * 0x200
        if: image_size != 0xffffffff
      audio_raw:
        pos: audio_start_address
        size: audio_size * 0x200
        if: audio_size != 0xffffffff

  content_struct:
    seq:
      - id: nbr_stories
        type: u2
      - id: stories
        type: story_struct
        repeat: expr
        repeat-expr: nbr_stories

  story_info_struct:
    seq:
      - id: nbr_nodes
        type: u2
      - id: factory_disabled
        type: u1
      - id: version
        type: u2
      - id: padding
        size: 0x200 - 5 #TODO this must be reworked
      - id: nodes
        type: node_struct
        repeat: expr
        repeat-expr: nbr_nodes

  story_struct:
    seq:
      - id: start_address
        type: u4
      - id: size
        type: u4
      - id: unknown
        type: u4
    instances:
      abs_start_address:
        value: _root.fileoffset + (start_address * 0x200)
      story_info:
        pos: abs_start_address
        type: story_info_struct
