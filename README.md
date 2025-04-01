# Rie's World Clock

## Overview
Rie's World Clock is a Python-based graphical application that displays the current time for multiple locations of my friends and family worldwide. It uses the Tkinter library for the GUI, `pytz` for timezone handling, and PIL for displaying country flags.

## Time Zones & Flags
The application displays time for the following locations:
- **Istanbul, Turkey** (KCHAN) 🇹🇷
- **Pacific Time, USA** (CHERISHIE) 🇺🇸
- **Dublin, Ireland** (SHARON) 🇮🇪
- **Sydney, Australia** (DAN) 🇦🇺
- **Tokyo, Japan** (ME!) 🇯🇵
- **Bangkok, Thailand** (DAY) 🇹🇭

Each location includes a label for the person's name, a digital clock, and a flag.

<img width="795" alt="Screenshot 2025-04-01 at 21 05 42" src="https://github.com/user-attachments/assets/8edc2d97-b268-4c9d-b477-11b985eacfa9" />

## Requirements
Make sure you have the following dependencies installed:
```bash
pip install pytz pillow
```
## Installation & Usage
1. Clone or download the project files.
2. Ensure you have Python installed.
3. Run the script:
   ```bash
   python world_clock.py
   ```
   
## Notes
- Ensure the image paths for the flags are correct before running the script.
- Modify the `timezones` list to add or remove locations.

