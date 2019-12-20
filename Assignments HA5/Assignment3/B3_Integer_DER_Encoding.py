import binascii
from math import ceil

value = hex(int(input("Please input the integer to encode: "))).lstrip('0x')
if not len(value) % 2 == 0:
    value = value.zfill(len(value) + 1)

byte_value = b'\x00' + bytearray.fromhex(value)
byte_value_length = len(byte_value)

if byte_value_length < 128:
    len_bytes = bytearray.fromhex(hex(byte_value_length).lstrip('0x').zfill(2))
else:
    bytes_needed = ceil(len(bin(byte_value_length).lstrip('0b')) / 8)
    len_bits = '1' + bin(bytes_needed).lstrip('0b').zfill(7) + bin(byte_value_length).lstrip('0b').zfill(8 * bytes_needed)
    len_hex = hex(int(len_bits, 2)).lstrip('0x')
    if not len(len_hex) % 2 == 0:
        len_hex = value.zfill(len(len_hex) + 1)  # for example, 8 needs to be 08 for bytearray.fromhex to work.
    len_bytes = bytearray.fromhex(len_hex)

byte_value = b'\x02' + len_bytes + byte_value

print(binascii.b2a_hex(byte_value).decode())
