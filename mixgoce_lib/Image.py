"""
Image

CircuitPython library for Image - MixGoCE
=======================================================

Small Cabbage
20210721
"""

HEART=bytearray(b'\x00\x00\x00\x0c\x1e\x3f\x7e\xfc\x7e\x3f\x1e\x0c\x00\x00\x00\x00')
HEART_SMALL=bytearray(b'\x00\x00\x00\x00\x0c\x1e\x3c\x78\x3c\x1e\x0c\x00\x00\x00\x00\x00')
HAPPY=bytearray(b'\x00\x00\x00\x0c\x0c\x20\x40\x80\x80\x40\x20\x0c\x0c\x00\x00\x00')
SAD=bytearray(b'\x00\x00\x08\x04\x04\x84\x40\x20\x20\x40\x84\x04\x04\x08\x00\x00')
SMILE=bytearray(b'\x00\x00\x04\x02\x02\x24\x40\x80\x80\x40\x24\x02\x02\x04\x00\x00')
SILLY=bytearray(b'\x00\x00\x04\x0a\x0a\x04\x60\xa0\xa0\x60\x04\x0a\x0a\x04\x00\x00')
FABULOUS=bytearray(b'\x00\x00\x06\x05\x05\x65\xa6\xa0\xa0\xa6\x65\x05\x05\x06\x00\x00')
SURPRISED=bytearray(b'\x00\x00\x00\x00\x00\x00\x00\xbe\x00\x00\x00\x00\x00\x00\x00\x00')
ASLEEP=bytearray(b'\x00\x00\x04\x04\x04\x44\xa0\xa0\xa0\xa0\x44\x04\x04\x04\x00\x00')
ANGRY=bytearray(b'\x00\x00\x01\x02\x84\x42\x21\x10\x10\x21\x42\x84\x02\x01\x00\x00')
CONFUSED=bytearray(b'\x00\x00\x00\x00\x00\x04\x02\xa2\x12\x0c\x00\x00\x00\x00\x00\x00')
NO=bytearray(b'\x00\x00\x00\x00\x42\x24\x18\x18\x24\x42\x00\x00\x00\x00\x00\x00')
YES=bytearray(b'\x00\x00\x00\x00\x10\x20\x40\x40\x20\x10\x08\x04\x02\x00\x00\x00')
LEFT_ARROW=bytearray(b'\x00\x00\x10\x28\x54\x92\x10\x10\x10\x10\x10\x10\x10\x10\x00\x00')
RIGHT_ARROW=bytearray(b'\x00\x00\x10\x10\x10\x10\x10\x10\x10\x10\x92\x54\x28\x10\x00\x00')
DRESS=bytearray(b'\x00\x00\x00\x40\xa2\xd7\xae\xda\xae\xd7\xa2\x40\x00\x00\x00\x00')
TRANSFORMERS=bytearray(b'\x00\x00\x00\x00\x00\x9c\x64\x1a\x64\x9c\x00\x00\x00\x00\x00\x00')
SCISSORS=bytearray(b'\x00\x00\x00\x00\x00\x43\xa6\x6c\x18\x6c\xa6\x43\x00\x00\x00\x00')
EXIT=bytearray(b'\x00\x00\x00\x00\x00\x00\x28\x04\x72\x0e\x17\x25\x48\x88\x00\x00')
TREE=bytearray(b'\x00\x00\x00\x10\x18\x1c\x1e\xff\x1e\x1c\x18\x10\x00\x00\x00\x00')
PACMAN=bytearray(b'\x00\x00\x1c\x36\x63\x41\x45\x41\x49\x55\x22\x00\x00\x00\x00\x00')
TARGET=bytearray(b'\x00\x00\x00\x00\x00\x00\x38\x44\x54\x44\x38\x00\x00\x00\x00\x00')
TSHIRT=bytearray(b'\x00\x00\x00\x04\x0a\xf9\x82\x82\x82\x82\xf9\x0a\x04\x00\x00\x00')
ROLLERSKATE=bytearray(b'\x00\x00\x00\x60\x5f\x71\x11\x17\x14\x14\x74\x58\x60\x00\x00\x00')
DUCK=bytearray(b'\x00\x00\x08\x0c\x0a\xf9\x81\x83\x9e\x90\x90\x90\x50\x30\x10\x00')
HOUSE=bytearray(b'\x04\x06\xfb\x01\x01\xf9\x09\x29\x09\x09\xf9\x01\x01\xfb\x06\x04')
TORTOISE=bytearray(b'\x00\x00\x00\x00\x00\x5e\x3c\x3f\x3f\x3c\x5e\x00\x00\x00\x00\x00')
BUTTERFLY=bytearray(b'\x00\x00\x00\x00\x04\xca\xaa\x5c\x38\x5c\xaa\xca\x04\x00\x00\x00')
STICKFIGURE=bytearray(b'\x00\x00\x00\x00\x00\x90\x4a\x3d\x4a\x90\x00\x00\x00\x00\x00\x00')
GHOST=bytearray(b'\x00\x00\x00\x00\xfe\xdf\xe9\xdf\xe9\xdf\xfe\xc0\x80\x00\x00\x00')
PITCHFORK=bytearray(b'\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x3e\x49\x49\x49\x49\x49')
MUSIC_QUAVERS=bytearray(b'\x20\x10\x08\x0c\x1c\x38\x30\x10\x08\x0c\x1c\x38\x30\x10\x08\x04')
MUSIC_QUAVER=bytearray(b'\x06\x05\x05\x05\x05\x05\x05\x05\x36\x7c\xfc\xfc\xf8\x70\x00\x00')
MUSIC_CROTCHET=bytearray(b'\x02\x02\x02\x02\x02\x02\x02\x02\x1a\x3e\x7e\x7e\x7c\x38\x00\x00')
COW=bytearray(b'\x00\x1e\x1a\x1f\xfe\xfc\x1c\x1c\x1c\xfc\xfc\x08\x10\x10\x20\x00')
RABBIT=bytearray(b'\x14\x2a\x2a\x2a\x2a\x2a\x63\x41\x55\x41\x49\x49\x5d\x41\x3e\x00')
SQUARE_SMALL=bytearray(b'\x00\x00\x00\x00\x00\x00\x3c\x24\x24\x3c\x00\x00\x00\x00\x00\x00')
SQUARE=bytearray(b'\x00\x00\x00\x00\xff\x81\x81\x81\x81\x81\x81\xff\x00\x00\x00\x00')
DIAMOND_SMALL=bytearray(b'\x00\x00\x00\x00\x00\x08\x14\x2c\x14\x08\x00\x00\x00\x00\x00\x00')
DIAMOND=bytearray(b'\x00\x00\x04\x0e\x1b\x35\x6f\xdd\x6f\x35\x1b\x0e\x04\x00\x00\x00')
CHESSBOARD=bytearray(b'\x00\x00\x00\xfe\xaa\xfe\xaa\xfe\xaa\xfe\xaa\xfe\xaa\xfe\x00\x00')
TRIANGLE_LEFT=bytearray(b'\x00\x00\x00\x00\x00\x10\x38\x7c\xfe\x00\x00\x00\x00\x00\x00\x00')
TRIANGLE=bytearray(b'\x00\x00\x40\x60\x70\x78\x7c\x7e\x7e\x7c\x78\x70\x60\x40\x00\x00')
SNAKE=bytearray(b'\x00\x40\x60\x70\x38\x18\x18\x18\x18\x1f\x05\x07\x00\x00\x00\x00')
UMBRELLA=bytearray(b'\x00\x00\x00\x08\x0c\x0e\x0e\xff\x8e\xce\x0c\x08\x00\x00\x00\x00')
SKULL=bytearray(b'\x00\x00\x00\x0c\x1a\x79\x99\xd7\x99\x79\x1a\x0c\x00\x00\x00\x00')
GIRAFFE=bytearray(b'\x00\x00\x00\x00\xe0\x20\x20\xff\x03\x02\x00\x00\x00\x00\x00\x00')
SWORD=bytearray(b'\x00\x00\x18\x18\x7e\x3c\x18\x18\x18\x18\x18\x18\x18\x00\x00\x00')