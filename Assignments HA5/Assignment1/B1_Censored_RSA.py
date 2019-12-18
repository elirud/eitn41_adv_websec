import asn1

with open('key.pem', 'r') as f:
    key = ''.join(f.read().splitlines())
key = str.encode(key)
decoder = asn1.Decoder()
decoder.start(key)
tag, value = decoder.read()
