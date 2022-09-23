enc = bytearray(open('basic4.webp', 'rb').read())

# 'RIFF'
riff = 0x52_49_46_46.to_bytes(4, 'big')
# 'WEBP'
webp = 0x57_45_42_50.to_bytes(4, 'big')

file_size = (len(enc) - 8).to_bytes(4, 'little')

# 'VP8'
vp8 = 0x56_50_38.to_bytes(3, 'big')

print("file size: %s / %i" % (hex(len(enc)), len(enc)))

header = riff + file_size + webp + vp8

size_key = len(header)
key = bytearray(size_key)

for i in range(size_key):
	key[i] = enc[i] ^ header[i]

key = bytes(key)
print("key: %s" % hex(int.from_bytes(key, 'big')))

size = len(enc)
decrypted = bytearray(len(enc))

for i in range(size):
	decrypted[i] = enc[i] ^ key[i % size_key]

open('res.webp', 'wb').write(decrypted)

# 0x773f763d_4d735161_5052324e
# w?v= usQa PR2N
