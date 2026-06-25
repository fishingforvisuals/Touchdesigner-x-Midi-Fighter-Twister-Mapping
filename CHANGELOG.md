# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Planned for v2+
- Support for different MIDI controllers
- Support for multiple banks and presets

### Planned for v1.0.0
- Dynamic project integration with relative references
- Enhanced documentation and examples

---

## [0.1.0] - 2026-06-25

### Added
- Core MIDI mapping functionality for Midi Fighter Twister controller
- Dynamic operator and parameter mapping via drag-and-drop UI
- Support for Midi Fighter Twister channels 1-16
- Knob color customization (UI and MIDI)
- Parameter labeling and recall functionality
- Settings persistence using `knob_settings` table
- Auto-load last parameter values on execute DAT start
- Integration with CHOP Execute DATs and scripts for MIDI/OSC workflows
- Multi-selection support for knobs (Shift for range, Ctrl for individual)
- Support for multiple use cases: installations, live performances, visual projects

### Known Limitations
- Paths require absolute references (relative path support planned for v1.0)
- Single bank/preset support (multi-bank support planned)
- Limited to Midi Fighter Twister controller (expansion planned)

---

[Unreleased]: https://github.com/fishingforvisuals/Touchdesigner-x-Midi-Fighter-Twister-Mapping/compare/v0.1.0...main
[0.1.0]: https://github.com/fishingforvisuals/Touchdesigner-x-Midi-Fighter-Twister-Mapping/releases/tag/v0.1.0
