#!/usr/bin/env python

# OTClient font template

from gimpfu import *

def otclient_font_create(font, size, height, width, color) :
    # New image
    image = gimp.Image(16*width, 14*height, RGB)

    # Text color
    gimp.set_foreground(color)

    charTableNr = [
        32, 33, 34, 35, 36, 37, 38, 39,
        40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
        50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
        60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
        70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
        80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
        90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
        100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
        110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
        120, 121, 122, 123, 124, 125, 126,
        9633,
        8364, 9633, 8218, 9633, 8222, 8230, 8224, 8225, 9633, 8240, 352, 8249, 346, 356, 381, 377,
        9633, 8216, 8217, 8220, 8221, 8226, 8211, 8212, 9633, 8482, 353, 8250, 347, 357, 382, 378,
        32, 711, 728, 321, 164, 260, 166, 167, 168, 169, 350, 171, 172, 32, 174, 379,
        176, 177, 731, 322, 180, 181, 182, 183, 184, 261, 351, 187, 317, 733, 318, 380,
        340, 193, 194, 258, 196, 313, 262, 199, 268, 201, 280, 203, 282, 205, 206, 270,
        272, 323, 327, 211, 212, 336, 214, 215, 344, 366, 218, 368, 220, 221, 354, 223,
        341, 225, 226, 259, 228, 314, 263, 231, 269, 233, 281, 235, 283, 237, 238, 271,
        273, 324, 328, 243, 244, 337, 246, 247, 345, 367, 250, 369, 252, 253, 355, 729
    ]

    charNr = 0

    for y in range(0, 14):
        for x in range(0, 16):
            fontChar = str(unichr(charTableNr[charNr]))
            charNr = charNr + 1
            layer = pdb.gimp_text_fontname(image, None, x*width, y*height, fontChar, 0, True, size, PIXELS, font)

    # Create window
    gimp.Display(image)
    # Show image window
    gimp.displays_flush()

register(
    "python_fu_otclient_font_create",
    "Create font for OTClient",
    "Create font for OTClient",
    "EgzoT",
    "EgzoT",
    "2018",
    "Otclient font create...",
    "",
    [
        (PF_FONT, "font", "Font", "Arial"),
        (PF_SPINNER, "size", "Font size", 20, (1, 3000, 1)),
        (PF_INT, "height", "Letter height", 20),
        (PF_INT, "width", "Letter width", 20),
        (PF_COLOUR, "color", "Text color", "#FFFFFF")
    ],
    [],
    otclient_font_create, menu="<Image>/File/Create")

main()