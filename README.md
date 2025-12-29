# Arthur-s-Macropad
Firmware:

This hackpad uses KMK firmware, a Python-based keyboard firmware that runs on CircuitPython and is well suited for small custom macropads.

The firmware is written for a Seeed XIAO RP2040 and uses direct GPIO scanning (no key matrix). Each of the five switches is connected to an individual GPIO pin and pulled to ground when pressed. The firmware scans these pins using KMK’s KeysScanner.

The project also includes support for two SK6812 MINI RGB LEDs, chained together and driven from a single data pin on the XIAO.

The firmware source can be found in the Firmware/ folder as main.py.
At submission time, the firmware has not been flashed to hardware, but it is logically complete and matches the PCB schematic and pinout.

Firmware stack:
Firmware: KMK
Language: Python
Runtime: CircuitPython
#BOM:
| Item              | Quantity | Part                                    | Notes                |
| ----------------- | -------- | --------------------------------------- | -------------------- |
| Microcontroller   | 1        | Seeed Studio XIAO RP2040 (Through-Hole) | Main MCU             |
| Mechanical Switch | 5        | MX-style switches                       | Input keys           |
| Keycaps           | 5        | DSA keycaps                             | Fits MX switches     |
| Diodes            | 5        | 1N4148 (Through-Hole)                   | Switch isolation     |
| RGB LEDs          | 2        | SK6812 MINI-E                           | Addressable RGB LEDs |
| PCB               | 1        | Custom 2-layer PCB                      | ≤ 100mm × 100mm      |
| Case (Top)        | 1        | 3D printed                              | PLA / PETG           |
| Case (Bottom)     | 1        | 3D printed                              | PLA / PETG           |
| Screws            | 4        | M3 × 16mm                               | Case assembly        |
| Heat-set Inserts  | 4        | M3 × 5mm × 4mm                          | Case mounting        |
| USB Cable         | 1        | USB-C cable                             | Programming & power  |



Overall HackPad overview:
I modeled the 5-key design in Fusion 360. The top and bottom are held together using 4 M3x16 bolts
<img width="1088" height="662" alt="image" src="https://github.com/user-attachments/assets/2ebaaf8d-0d09-439d-a297-84ff313e8ca2" />

The MCU used in the CAD model was imported from PTC's Onshape. It was fitted to a green rectangular part symbolizing the PCB
<img width="605" height="447" alt="image" src="https://github.com/user-attachments/assets/4d8add59-9c20-4ebb-9c13-a1bcf0674563" />

Top cover:
<img width="1249" height="641" alt="image" src="https://github.com/user-attachments/assets/54ba9ce4-ca23-4464-8002-34fcaf3426e7" />

Bottom with PCB and Bolts:
<img width="997" height="573" alt="image" src="https://github.com/user-attachments/assets/847b80da-665d-4b84-9062-2b13f75f42e5" />


PCB Images:
<img width="354" height="596" alt="image" src="https://github.com/user-attachments/assets/5f13845e-b8ab-4640-83f4-904b799ea131" />
<img width="944" height="740" alt="image" src="https://github.com/user-attachments/assets/1664261f-5f06-4820-898c-76561a1127ba" />
