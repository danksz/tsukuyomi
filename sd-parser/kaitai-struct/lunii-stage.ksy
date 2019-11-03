meta:
  id: luniistage
  file-extension: luniistage
  endian: be
instances:
  uuid:
    size: 16
  image_start_sector:
    type: u4
  image_size:
     type: u4
  image_start_sector:
    type: u4
  image_size:
     type: u4
  audio_start_sector:
    type: u4
  audio_size:
     type: u4

  #If the action is set but the chosen index is -1, then a random option of the list is selected.
  action_on_ok:
     type: u2
  option_in_transition:
     type: u2
  chosen_option:
     type: u2 
  wheel_enabled:
     type: u2 
  ok_enabled:
     type: u2

  #If HOME button is enabled but no action is set (i.e. all transition fields are -1), the user is directed all the way back to the main stage (story-pack selection).
  home_enabled:
     type: u2   
  paused_enabled:
     type: u2   
  autojump_at_audio_ends_enabled:
     type: u2   