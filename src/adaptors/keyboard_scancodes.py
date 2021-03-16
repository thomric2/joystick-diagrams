# SCANCODES from https://github.com/sethmlarson/virtualbox-python/virtualbox/library_ext/keyboard.html

# Define a scancode lookup dictionary
SCANCODES = {
    "ESC": [[0x01], [0x81]],
    "1": [[0x02], [0x82]],
    "!": [[0x2A, 0x02], [0x82, 0xAA]],
    "2": [[0x03], [0x83]],
    "@": [[0x2A, 0x03], [0x83, 0xAA]],
    "3": [[0x04], [0x84]],
    "#": [[0x2A, 0x04], [0x84, 0xAA]],
    "4": [[0x05], [0x85]],
    "$": [[0x2A, 0x05], [0x85, 0xAA]],
    "5": [[0x06], [0x86]],
    "%": [[0x2A, 0x06], [0x86, 0xAA]],
    "6": [[0x07], [0x87]],
    "^": [[0x2A, 0x07], [0x87, 0xAA]],
    "7": [[0x08], [0x88]],
    "&": [[0x2A, 0x08], [0x88, 0xAA]],
    "8": [[0x09], [0x89]],
    "*": [[0x2A, 0x09], [0x89, 0xAA]],
    "9": [[0x0A], [0x8A]],
    "(": [[0x2A, 0x0A], [0x8A, 0xAA]],
    "0": [[0x0B], [0x8B]],
    ")": [[0x2A, 0x0B], [0x8B, 0xAA]],
    "-": [[0x0C], [0x8C]],
    "_": [[0x2A, 0x0C], [0x8C, 0xAA]],
    "=": [[0x0D], [0x8D]],
    "+": [[0x2A, 0x0D], [0x8D, 0xAA]],
    "BKSP": [[0x0E], [0x8E]],
    "\b": [[0x0E], [0x8E]],
    "TAB": [[0x0F], [0x8F]],
    "\t": [[0x0F], [0x8F]],
    "q": [[0x10], [0x90]],
    "Q": [[0x2A, 0x10], [0x90, 0xAA]],
    "w": [[0x11], [0x91]],
    "W": [[0x2A, 0x11], [0x91, 0xAA]],
    "e": [[0x12], [0x92]],
    "E": [[0x2A, 0x12], [0x92, 0xAA]],
    "r": [[0x13], [0x93]],
    "R": [[0x2A, 0x13], [0x93, 0xAA]],
    "t": [[0x14], [0x94]],
    "T": [[0x2A, 0x14], [0x94, 0xAA]],
    "y": [[0x15], [0x95]],
    "Y": [[0x2A, 0x15], [0x95, 0xAA]],
    "u": [[0x16], [0x96]],
    "U": [[0x2A, 0x16], [0x96, 0xAA]],
    "i": [[0x17], [0x97]],
    "I": [[0x2A, 0x17], [0x97, 0xAA]],
    "o": [[0x18], [0x98]],
    "O": [[0x2A, 0x18], [0x98, 0xAA]],
    "p": [[0x19], [0x99]],
    "P": [[0x2A, 0x19], [0x99, 0xAA]],
    "[": [[0x1A], [0x9A]],
    "{": [[0x2A, 0x1A], [0x9A, 0xAA]],
    "]": [[0x1B], [0x9B]],
    "}": [[0x2A, 0x1B], [0x9B, 0xAA]],
    "ENTER": [[0x1C], [0x9C]],
    "\r": [[0x1C], [0x9C]],
    "\n": [[0x1C], [0x9C]],
    "CTRL": [[0x1D], [0x9D]],
    "a": [[0x1E], [0x9E]],
    "A": [[0x2A, 0x1E], [0x9E, 0xAA]],
    "s": [[0x1F], [0x9F]],
    "S": [[0x2A, 0x1F], [0x9F, 0xAA]],
    "d": [[0x20], [0xA0]],
    "D": [[0x2A, 0x20], [0xA0, 0xAA]],
    "f": [[0x21], [0xA1]],
    "F": [[0x2A, 0x21], [0xA1, 0xAA]],
    "g": [[0x22], [0xA2]],
    "G": [[0x2A, 0x22], [0xA2, 0xAA]],
    "h": [[0x23], [0xA3]],
    "H": [[0x2A, 0x23], [0xA3, 0xAA]],
    "j": [[0x24], [0xA4]],
    "J": [[0x2A, 0x24], [0xA4, 0xAA]],
    "k": [[0x25], [0xA5]],
    "K": [[0x2A, 0x25], [0xA5, 0xAA]],
    "l": [[0x26], [0xA6]],
    "L": [[0x2A, 0x26], [0xA6, 0xAA]],
    ";": [[0x27], [0xA7]],
    ":": [[0x2A, 0x27], [0xA7, 0xAA]],
    "'": [[0x28], [0xA8]],
    '"': [[0x2A, 0x28], [0xA8, 0xAA]],
    "`": [[0x29], [0xA9]],
    "~": [[0x2A, 0x29], [0xA9, 0xAA]],
    "LSHIFT": [[0x2A], [0xAA]],
    "\\": [[0x2B], [0xAB]],
    "|": [[0x2A, 0x2B], [0xAB, 0xAA]],
    "z": [[0x2C], [0xAC]],
    "Z": [[0x2A, 0x2C], [0xAC, 0xAA]],
    "x": [[0x2D], [0xAD]],
    "X": [[0x2A, 0x2D], [0xAD, 0xAA]],
    "c": [[0x2E], [0xAE]],
    "C": [[0x2A, 0x2E], [0xAE, 0xAA]],
    "v": [[0x2F], [0xAF]],
    "V": [[0x2A, 0x2F], [0xAF, 0xAA]],
    "b": [[0x30], [0xB0]],
    "B": [[0x2A, 0x30], [0xB0, 0xAA]],
    "n": [[0x31], [0xB1]],
    "N": [[0x2A, 0x31], [0xB1, 0xAA]],
    "m": [[0x32], [0xB2]],
    "M": [[0x2A, 0x32], [0xB2, 0xAA]],
    ",": [[0x33], [0xB3]],
    "<": [[0x2A, 0x33], [0xB3, 0xAA]],
    ".": [[0x34], [0xB4]],
    ">": [[0x2A, 0x34], [0xB4, 0xAA]],
    "/": [[0x35], [0xB5]],
    "?": [[0x2A, 0x35], [0xB5, 0xAA]],
    "RSHIFT": [[0x36], [0xB6]],
    "PRTSC": [[0x37], [0xB7]],
    "ALT": [[0x38], [0xB8]],
    "SPACE": [[0x39], [0xB9]],
    " ": [[0x39], [0xB9]],
    "CAPS": [[0x3A], [0xBA]],
    "F1": [[0x3B], [0xBB]],
    "F2": [[0x3C], [0xBC]],
    "F3": [[0x3D], [0xBD]],
    "F4": [[0x3E], [0xBE]],
    "F5": [[0x3F], [0xBF]],
    "F6": [[0x40], [0xC0]],
    "F7": [[0x41], [0xC1]],
    "F8": [[0x42], [0xC2]],
    "F9": [[0x43], [0xC3]],
    "F10": [[0x44], [0xC4]],
    "F11": [[0x57], [0xD7]],
    "F12": [[0x58], [0xD8]],
    "NUM": [[0x45], [0xC5]],
    "SCRL": [[0x46], [0xC6]],
    "HOME": [[0x47], [0xC7]],
    "UP": [[0x48], [0xC8]],
    "PGUP": [[0x49], [0xC9]],
    "MINUS": [[0x4A], [0xCA]],
    "LEFT": [[0x4B], [0xCB]],
    "CENTER": [[0x4C], [0xCC]],
    "RIGHT": [[0x4D], [0xCD]],
    "PLUS": [[0x4E], [0xCE]],
    "END": [[0x4F], [0xCF]],
    "DOWN": [[0x50], [0xD0]],
    "PGDN": [[0x51], [0xD1]],
    "INS": [[0x52], [0xD2]],
    "DEL": [[0x53], [0xD3]],
    "E_DIV": [[0xE0, 0x54], [0xE0, 0xD4]],
    "E_ENTER": [[0xE0, 0x1C], [0xE0, 0x9C]],
    "E_INS": [[0xE0, 0x52], [0xE0, 0xD2]],
    "E_DEL": [[0xE0, 0x53], [0xE0, 0xD3]],
    "E_HOME": [[0xE0, 0x47], [0xE0, 0xC7]],
    "E_END": [[0xE0, 0x4F], [0xE0, 0xCF]],
    "E_PGUP": [[0xE0, 0x49], [0xE0, 0xC9]],
    "E_PGDN": [[0xE0, 0x51], [0xE0, 0xD1]],
    "E_LEFT": [[0xE0, 0x4B], [0xE0, 0xCB]],
    "E_RIGHT": [[0xE0, 0x4D], [0xE0, 0xCD]],
    "E_UP": [[0xE0, 0x48], [0xE0, 0xC8]],
    "E_DOWN": [[0xE0, 0x50], [0xE0, 0xD0]],
    "RALT": [[0x0C, 0x38], [0xC0, 0xB8]],
    "RCTRL": [[0x0C, 0x1D], [0xC0, 0x9D]],
    "LWIN": [[0xE0, 0x5B], [0xE0, 0xDB]],
    "RWIN": [[0xE0, 0x5C], [0xE0, 0xDC]],
    # No scan code for pause key released
    "PAUSE": [[0xE1, 0x1D, 0x45, 0xE1, 0x9D, 0xC5], []],
}


# Build the lookup tree.
LOOKUP = {}
OFF = 0
ON = 1


def _is_shift_key(c):
    return len(c[0]) == 2 and c[0][0] == 0x2A


for key, codes in SCANCODES.items():
    if _is_shift_key(codes):
        continue
    down, up = codes
    node = LOOKUP
    for code in down:
        node = node.setdefault(code, {})
    node["leaf"] = [ON, key]
    node = LOOKUP
    for code in up:
        node = node.setdefault(code, {})
    node["leaf"] = [OFF, key]


# Lock in duplicate key values to chosen types below:
LOOKUP[0x1C]["leaf"][1] = "NEWLINE"
LOOKUP[0x9C]["leaf"][1] = "NEWLINE"
LOOKUP[0x0E]["leaf"][1] = "BKSP"
LOOKUP[0x8E]["leaf"][1] = "BKSP"
LOOKUP[0x0F]["leaf"][1] = "TAB"
LOOKUP[0x8F]["leaf"][1] = "TAB"
LOOKUP[0x39]["leaf"][1] = "SPACE"
LOOKUP[0xB9]["leaf"][1] = "SPACE"
LOOKUP[0xB8]["leaf"][1] = "ALT"
LOOKUP[0x9D]["leaf"][1] = "CTRL"


# Build the shift state key lookup.
KEY_TO_CAPS = {}
for caps_key, codes in SCANCODES.items():
    if not _is_shift_key(codes):
        continue
    key = LOOKUP[codes[0][1]]["leaf"][1]
    KEY_TO_CAPS[key] = caps_key

