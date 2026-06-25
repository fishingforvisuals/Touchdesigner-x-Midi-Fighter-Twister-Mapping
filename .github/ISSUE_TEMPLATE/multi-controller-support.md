---
name: Multi-Controller Support
about: Track progress on expanding mapping methods to new controllers
title: "Expand mapping methods to support additional MIDI controllers"
---

## Overview

Extend the portable mapping methodology developed for the MIDI Fighter Twister to additional MIDI controllers that are currently available in the studio. This will enable consistent, reusable mapping patterns across different hardware.

## Supported Controllers

- Novation Launch Control XL 3
- Novation Launchpad Mini 3
- Novation Launchkey 37 MK3

## Goals

- Adapt the portability and relative reference methods to work with each controller's unique MIDI specification
- Create modular, reusable mapping templates for each controller type
- Apply the same principles of banks, presets, and configurable parameters across all controllers
- Maintain consistency in the TouchDesigner workflow regardless of which controller is used

## Requirements

- Map each controller's hardware layout to TouchDesigner operations
- Ensure relative references and portable paths work across all controller implementations
- Create documentation for each controller's specific features and mappings
- Allow users to switch between controllers with minimal configuration changes

## Benefits

- Establishes a framework for adding more controllers in the future
- Provides flexibility for multi-controller setups
- Reuses proven mapping methodologies across different hardware
- Reduces development time for future controller support
