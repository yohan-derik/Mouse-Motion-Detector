# Mouse Motion Detector

A Python application that opens a window and detects when your mouse hovers over it, playing continuous beeping sound as feedback.

## Features

- Opens a simple white window
- Continuously monitors mouse position
- Plays 1000 Hz beeping sound when mouse hovers over the window
- Multiple beeps can overlap for uninterrupted audio feedback
- Beeping stops when you move the mouse away

## Requirements

- Python 3.6+
- `pynput` library for mouse tracking

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yohan-derik/Mouse-Motion-Detector.git
cd Mouse-Motion-Detector
```

2. Install the required dependency:
```bash
pip install pynput
```

## Usage

Run the script:
```bash
python mouse_hover_detector.py
```

A white window will appear. Move your mouse over it to hear the beeping sound. Move your mouse away to stop the sound.

## Technical Details

- **GUI**: tkinter (built-in with Python)
- **Mouse Tracking**: pynput
- **Audio**: Windows `winsound` module (Windows only)