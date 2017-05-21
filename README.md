# ALE Tracker

> Consider using [gym-tracker](http://github.com/alvinwan/gym-tracker) instead. This codebase pauses the game when you take actions. However, the `gym-tracker` features continuous gameplay.

Tracks actions for a human player, when manual control mode via ALE is not
available.

# Install

See offsite [installation instructions](http://alvinwan.com/installing-arcade-learning-environment-with-python3-on-macosx/).

# Usage

Say your rom is at `~/Downloads/space_invaders.bin`. To start logging, run

```
python main.py ~/Downloads/space_invaders.bin --user --display
```
