# Touchdesigner-x-Midi-Fighter-Twister-Mapping
A TouchDesigner module for mapping knob values onto a midi controller. Parameters can be updated dynamically per drag and drop functionality. It will store the last settings of the knobs but the actual storage handling should be managed by the vj software were it sits in.

--- 
## ✨ Features
- uses ch1-16 of Midi Fighter Twister to map on
- Dynamic operator + parameter mapping via drag and drop functionality onto UI knobs
- Store and recall functionality for last parameter values (`knob_settings` table) on start() and exit() of execute DAT 
- Easy integration with **CHOP Execute DATs** or scripts for MIDI/OSC workflows  
- basic recall of last settings
<!-- TODO: make paths relative or add a settings page where base path can be defined to prepare the tox -->

---

## ⚙️ core
- **`MidiControllerEXT` class** provides methods:  
  - `ChangeKnobColor()` → changes ui and midi colors per knob  
  - `LabelKnob()` → recalls and applies stored mappings  

## How to use
- drag parameters onto a ui knob to assign it to it
- click onto ui knobs to select knobs and change settings in the parameter viewer section. Use these keys for multiselection:
    - shift: range of knobs
    - ctrl: add or remove single knobs 

---

## 🎛️ Use Cases
- MIDI or OSC controlled installations  
- Live performance setups with dynamic mapping  
- Visual projects requiring quick reset + recall of parameter states

## Features to come:
<!-- TODO: this basic patch could still handle: more banks and presets  -->
- support more banks and presets
- support for different midi controllers
- support for dynamic integration into projects (with relative references or a settings page to define the base path) and a tox version