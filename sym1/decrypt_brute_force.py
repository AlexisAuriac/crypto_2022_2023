#!/bin/env python3

import base64
import hashlib

from Crypto.Cipher import AES

bs = AES.block_size
plaintext = "I was lost, but now I'm found..."
key = hashlib.sha256("omgwtfbbq".encode()).digest()

# __f374a82db50b23_____b88f1d976ddc1cf6db4524aac04e222853969367e0d
# cbc_known = 0xf374a82db50b23.to_bytes(7, 'big')
cbc_known = 0x00f374a82db50b2300000b88f1d976dd.to_bytes(16, 'big')

# iv = "________________".encode()

ecb_cipher = AES.new(key, AES.MODE_ECB)
# ecb_ciphertext = ecb_cipher.encrypt(plaintext.encode())
ecb_dec = ecb_cipher.decrypt(cbc_known)

def bytes_hex(bytes):
	return ''.join(format(x, '02x') for x in bytes)

# iv = plaintext.encode()[:8]
iv = bytearray(16)

# print(bytes_hex(cbc_known))
print(bytes_hex(plaintext.encode()))

for i in range(16):
	iv[i] = plaintext.encode()[i] ^ cbc_known[i] ^ key[i]
	# iv[i] = ecb_dec[i] ^ plaintext.encode()[i]

for i in range(2 ** 8): # 2 bytes of data
	cbc_missing = i.to_bytes(1, 'big')
	cbc = cbc_missing + cbc_known

	potential_iv = bytearray(8)

	for i in range(8):
		potential_iv[i] = ecb_ciphertext[i] ^ cbc[i]

	potential_iv = bytes(potential_iv)	

	cbc_cipher = AES.new(key, AES.MODE_CBC, potential_iv)
	cbc_ciphertext = cbc_cipher.encrypt(plaintext.encode())

	error = False

	for i in range(2, 8):
		if cbc_ciphertext[i] != cbc_known[i - 1]:
			error = True
			break

	if not error:
		print("iv:")
		print(''.join(format(x, '02x') for x in potential_iv))
		exit(0)


print("iv not found")
exit(1)
