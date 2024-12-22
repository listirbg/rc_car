# ################################################
# Bilder als Bytearray in Funktionen abgespeichert
# ################################################

# Logo Speedster
def logo() -> bytearray:
    return bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xcc, 0xdc, 0x98, 0x98, 0x60, 0x60, 0x60, 0x98, 0x98,
        0xdc, 0x30, 0x30, 0x30, 0xcc, 0xce, 0xce, 0x38, 0x30, 0x30, 0x00, 0xf8, 0xfc, 0xfc, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x07, 0x07,
        0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07,
        0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07,
        0x07, 0x07, 0x07, 0x07, 0x02, 0x00, 0x00, 0x0c, 0x0c, 0x19, 0x19, 0x06, 0x06, 0x06, 0x19, 0x19,
        0x19, 0x07, 0x03, 0x03, 0x0c, 0x0c, 0x0c, 0x03, 0x03, 0x07, 0x00, 0xff, 0xff, 0xff, 0x02, 0x07,
        0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07,
        0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07,
        0x07, 0x07, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x06, 0x07, 0x07, 0x87,
        0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0x07, 0x07, 0x07, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7,
        0xc7, 0x87, 0x07, 0x07, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0x07, 0x07, 0x06,
        0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0x07, 0x07, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7,
        0xc7, 0xc7, 0x87, 0x07, 0x07, 0x07, 0x06, 0xc6, 0xc6, 0xc6, 0xc6, 0xc7, 0xc7, 0xc7, 0xc7, 0x06,
        0x07, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0x07, 0xc7, 0xc7, 0xc7, 0xc7,
        0xc7, 0xc7, 0xc7, 0xc7, 0x07, 0x07, 0x07, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0xc7, 0x87,
        0x07, 0x07, 0x07, 0x07, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff,
        0xff, 0xff, 0xc1, 0xc1, 0xcf, 0xcf, 0xcf, 0x0f, 0x00, 0x00, 0xff, 0xff, 0xff, 0x01, 0x81, 0xff,
        0xff, 0xff, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0xc1, 0xc1, 0xc1, 0xc1, 0x01, 0x00, 0x00, 0x00,
        0xff, 0xff, 0xff, 0xc1, 0xc1, 0xc1, 0xc1, 0x01, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0x01, 0x01,
        0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0xc1, 0xc1, 0xcf, 0xcf, 0xc7, 0x80,
        0x00, 0x03, 0x03, 0x01, 0xff, 0xff, 0xff, 0xff, 0x01, 0x03, 0x03, 0x00, 0xff, 0xff, 0xff, 0xff,
        0xc1, 0xc1, 0xc1, 0xc1, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0x81, 0x81, 0xff, 0xff, 0xff, 0xff,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x70, 0xf1,
        0xf3, 0xf1, 0xc1, 0xc1, 0xff, 0xff, 0xff, 0x7f, 0x00, 0x00, 0xff, 0xff, 0xff, 0x07, 0x07, 0x07,
        0x07, 0x03, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xe1, 0xe1, 0xe1, 0xe0, 0x00, 0x00, 0x00,
        0xff, 0xff, 0xff, 0xe1, 0xe1, 0xe1, 0xe1, 0xe0, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0xe0, 0xe0,
        0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x78, 0xf9, 0xf9, 0xf9, 0xe1, 0xe1, 0xff, 0xff, 0xff, 0x3f,
        0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff,
        0xe1, 0xe1, 0xe1, 0xe1, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0x03, 0x1f, 0xff, 0xff, 0xfb, 0xc1,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x30, 0x70, 0x70, 0x70, 0x71,
        0x71, 0x71, 0x71, 0x71, 0x71, 0x71, 0x70, 0x70, 0x70, 0x70, 0x73, 0x73, 0x73, 0x70, 0x70, 0x70,
        0x70, 0x70, 0x70, 0x70, 0x71, 0x71, 0x71, 0x71, 0x71, 0x71, 0x71, 0x71, 0x71, 0x70, 0x70, 0xf1,
        0xf1, 0xf1, 0x71, 0xf1, 0xf1, 0x71, 0x71, 0x71, 0x70, 0x70, 0x71, 0x71, 0x71, 0x71, 0x71, 0x71,
        0x71, 0x71, 0x70, 0x70, 0x70, 0x70, 0x70, 0x70, 0x71, 0x71, 0xf1, 0xf1, 0xf1, 0x70, 0xf0, 0xf0,
        0x70, 0x70, 0x70, 0x70, 0x71, 0x71, 0x71, 0x71, 0x70, 0x70, 0x70, 0x70, 0x70, 0x70, 0x70, 0x71,
        0x71, 0x71, 0x71, 0x71, 0x70, 0x70, 0x71, 0x71, 0x71, 0x73, 0x70, 0x70, 0x70, 0x73, 0x73, 0x73,
        0x72, 0x70, 0x70, 0x70, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x30, 0x30, 0x30,
        0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30,
        0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x33,
        0x3f, 0x7f, 0xf8, 0xe7, 0x9f, 0x3e, 0x78, 0xe0, 0xc0, 0x80, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x80, 0x80, 0xc0, 0xe0, 0x70, 0x3c, 0x9f, 0xe7, 0xf0, 0x7e, 0x3f, 0x37,
        0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30,
        0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30,
        0x30, 0x30, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x01, 0x03, 0x07, 0x0e, 0x0e, 0x1d, 0x1d, 0x1b, 0x3b, 0x3b, 0x37, 0x37, 0x37,
        0x37, 0x37, 0x33, 0x3b, 0x1b, 0x19, 0x1d, 0x0e, 0x0e, 0x07, 0x03, 0x01, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ])


# Tacho 30x30 px
def tacho_30x30() -> bytearray:
    return bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x80, 0x80,
        0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x80, 0xe0, 0xf0, 0x38, 0x3c, 0x2c, 0x0e, 0x06, 0x0f, 0x03, 0x03, 0x03, 0x07, 0x07, 0x03, 0x03,
        0x03, 0x0f, 0x86, 0xce, 0x64, 0x20, 0x10, 0xc0, 0xc0, 0x80, 0x00, 0x00, 0x00, 0x7c, 0x7f, 0x07,
        0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x70, 0x78, 0x3c, 0x1c, 0x0e, 0x03,
        0x01, 0x00, 0x00, 0x00, 0x00, 0x03, 0x07, 0x7f, 0x7c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ])


# Tacho max. 20x20 px
def tacho_max_20x20() -> bytearray:
    return bytearray([
        0x00, 0x80, 0xc0, 0x60, 0x30, 0x18, 0x18, 0x0c, 0x0c, 0x0c, 0x0c, 0x0c, 0x0c, 0x98, 0xd8, 0x00,
        0x00, 0xc0, 0x80, 0x00, 0x00, 0x8f, 0x41, 0x40, 0x80, 0x40, 0x40, 0x80, 0x00, 0x48, 0x4c, 0x46,
        0xc3, 0x01, 0x40, 0x80, 0x00, 0x81, 0x4f, 0x00, 0x00, 0x07, 0x00, 0x00, 0x07, 0x00, 0x00, 0x07,
        0x00, 0x07, 0x05, 0x05, 0x07, 0x00, 0x04, 0x02, 0x01, 0x02, 0x04, 0x00
    ])


# Verbindung 0 16x16 px
def connection_0_16x16() -> bytearray:
    return bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0x20, 0x20, 0xe0, 0x00, 0x00, 0xff, 0x01, 0x01, 0xff,
        0xfc, 0x84, 0x84, 0xfc, 0x00, 0x00, 0xff, 0x80, 0x80, 0xff, 0x00, 0x00, 0xff, 0x80, 0x80, 0xff
    ])


# Verbindung 1 16x16 px
def connection_1_16x16() -> bytearray:
    return bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0x20, 0x20, 0xe0, 0x00, 0x00, 0xff, 0x01, 0x01, 0xff,
        0xfc, 0xfc, 0xfc, 0xfc, 0x00, 0x00, 0xff, 0x80, 0x80, 0xff, 0x00, 0x00, 0xff, 0x80, 0x80, 0xff
    ])


# Verbindung 2 16x16 px
def connection_2_16x16() -> bytearray:
    return bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0xe0, 0xe0, 0xe0, 0x00, 0x00, 0xff, 0x01, 0x01, 0xff,
        0xfc, 0xfc, 0xfc, 0xfc, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0xff, 0x80, 0x80, 0xff
    ])


# Verbindung 3 16x16 px
def connection_3_16x16() -> bytearray:
    return bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0xe0, 0xe0, 0xe0, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff,
        0xfc, 0xfc, 0xfc, 0xfc, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff
    ])
