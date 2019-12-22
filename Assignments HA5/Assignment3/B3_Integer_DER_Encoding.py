import binascii
from math import ceil


def egcd(e, squiggly_symbol):
    r1, r2 = squiggly_symbol, e
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 != 0:
        quotient = r1 // r2
        r2t, s2t, t2t = r2, s2, t2
        r2 = r1 - quotient * r2t
        s2 = s1 - quotient * s2t
        t2 = t1 - quotient * t2t
        r1 = r2t
        s1 = s2t
        t1 = t2t
    return t1 % squiggly_symbol


def der_encode(tag, value):
    if not len(value) % 2 == 0:  # for example, 8 needs to be 08 for bytearray.fromhex to work.
        value = value.zfill(len(value) + 1)

    byte_value = bytearray.fromhex(value)
    if bin(int(value, 16)).lstrip('0b').zfill(len(byte_value * 8))[0] == '1':
        byte_value = b'\x00' + byte_value

    byte_value_length = len(byte_value)

    if byte_value_length < 128:
        len_bytes = bytearray.fromhex(hex(byte_value_length).lstrip('0x').zfill(2))
    else:
        bytes_needed = ceil(len(bin(byte_value_length).lstrip('0b')) / 8)
        len_bits = '1' + bin(bytes_needed).lstrip('0b').zfill(7) + bin(byte_value_length).lstrip('0b').zfill(8 * bytes_needed)
        len_hex = hex(int(len_bits, 2)).lstrip('0x')
        if not len(len_hex) % 2 == 0:
            len_hex = value.zfill(len(len_hex) + 1)
        len_bytes = bytearray.fromhex(len_hex)

    return tag + len_bytes + byte_value


int_value = hex(int(input("Please input the integer to encode: "))).lstrip('0x')
print(binascii.b2a_hex(der_encode(b'\x02', int_value)).decode())

p = 99542050115101631342178164306213015285723136934260590047263876670745773827319743222077367628956731202527345960255773757387432271507934500418970906013080950660195221786056198414470733498607527928533391223748668331815697263026184122808523864310600074019136953195178741361019228430642873362764242203111144884893
q = 115589790247990023721222212575051402524954942258608344900848204326931314059264808170583277453555931173163510144371622752090146825245201971902979913384030890183280606804480896307654116743967549214610987905657673212122927299967349561267308121396763539327996046845551250958460141682522431042204148582930467913563
e = 65537
n = p * q
squiggly_symbol = (p - 1) * (q - 1)

d = egcd(e, squiggly_symbol)
exp1 = d % (p - 1)
exp2 = d % (q - 1)
c = pow(q, p - 2, p)

encoded_values = [binascii.b2a_hex(der_encode(b'\x02', hex(x).lstrip('0x'))).decode() for x in [n, e, d, p, q, exp1, exp2, c]]
seq = '020100' + ''.join(encoded_values)

print(binascii.b2a_base64(der_encode(b'\x30', seq)).decode())
