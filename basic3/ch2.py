import sys

# enc = bytearray(open('example.bmp', 'rb').read())
enc = bytearray(open('ch2.bmp', 'rb').read())

# key_b = 0x6769.to_bytes(2, 'big')
# key_b = 0x67697467.to_bytes(4, 'big')
key_b = 0x6769_7467_7564.to_bytes(6, 'big')

size = len(enc)
decrypted = bytearray(len(enc))

for i in range(size):
	decrypted[i] = enc[i] ^ key_b[i % len(key_b)]

open('res.bmp', 'wb').write(decrypted)

print(hex(len(enc)))
print(len(key_b))
