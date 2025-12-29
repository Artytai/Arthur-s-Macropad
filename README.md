# Arthur-s-Macropad
Firmware

This hackpad uses KMK firmware, a Python-based keyboard firmware that runs on CircuitPython and is well suited for small custom macropads.

The firmware is written for a Seeed XIAO RP2040 and uses direct GPIO scanning (no key matrix). Each of the five switches is connected to an individual GPIO pin and pulled to ground when pressed. The firmware scans these pins using KMK’s KeysScanner.

The project also includes support for two SK6812 MINI RGB LEDs, chained together and driven from a single data pin on the XIAO.

The firmware source can be found in the Firmware/ folder as main.py.
At submission time, the firmware has not been flashed to hardware, but it is logically complete and matches the PCB schematic and pinout.

Firmware stack:

Firmware: KMK

Language: Python

Runtime: CircuitPython

MCU: Seeed XIAO RP2040
