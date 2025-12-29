import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

from kmk.extensions.led import LED
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

# -------------------------
# Switch pins (match PCB)
# -------------------------
PINS = [
    board.GP26,  # SW1
    board.GP27,  # SW2
    board.GP28,  # SW3
    board.GP29,  # SW4
    board.GP6,   # SW5
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# -------------------------
# Keymap
# -------------------------
keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
        KC.E,
    ]
]

# -------------------------
# RGB LEDs (2x SK6812 MINI)
# -------------------------
rgb = RGB(
    pixel_pin=board.GP0,  # TX pin → LED DIN
    num_pixels=2,
    val_limit=100,
    hue_default=0,
    sat_default=255,
    val_default=50,
)

keyboard.extensions.append(rgb)

# -------------------------
# Start KMK
# -------------------------
if __name__ == '__main__':
    keyboard.go()
