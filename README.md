# Touchdesigner-x-Midi-Fighter-Twister-Mapping
A TouchDesigner module for mapping knob values onto a midi controller. Parameters can be updated dynamically per drag and drop functionality. It will store the last settings of the knobs but the actual storage handling should be managed by the vj software were it sits in.

---
<!-- TODO: update features and how it works --> 
## ✨ Features
- Dynamic operator + parameter mapping via lookup tables  
- Store and recall functionality for parameter values (`midi_assignments` table)  
- Reset system to clear all knob values before applying stored mappings (`opfind1` table)  
- Easy integration with **CHOP Execute DATs** or scripts for MIDI/OSC workflows  
- Clean, object-oriented structure using TouchDesigner’s `EXT` class convention  
<!-- TODO: this basic patch could still handle: more banks, and resets, basic recal of last settings -->

---

## ⚙️ How it Works
- **`opfind1` table** → lists all knobs and their parameters (used for reset)  

- **`MainEXT` class** provides methods:  
  - `reset_knobs()` → clears all knobs to a default value  
  - `apply_assignments()` → recalls and applies stored mappings  
  - `store_data()` → updates an individual parameter dynamically  

---

## 🎛️ Use Cases
- MIDI or OSC controlled installations  
- Live performance setups with dynamic mapping  
- Visual projects requiring quick reset + recall of parameter states  

---

## 📖 Example Workflow
```python
# Reset all knobs to default
op('base1').ext.Main.reset_knobs()

# Apply stored assignments
op('base1').ext.Main.apply_assignments()

# Update a single knob dynamically
op('base1').ext.Main.store_data("knob1", "Knoblevelcolorr", 0.5)


Visual projects requiring quick reset + recall of parameter states
