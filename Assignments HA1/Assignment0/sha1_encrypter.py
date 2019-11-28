import hashlib

def integer_to_hexadecimal(istring):
    return str(hex(istring))

def hexadecimal_to_integer(hstring):
    return str(int(hstring, 16))

def sha1_hash_hexadecimal_value(hstring):
    return str(hashlib.sha1(hstring))
