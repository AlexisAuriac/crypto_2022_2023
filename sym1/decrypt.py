#!/bin/env python3

import base64
import hashlib

from Crypto.Cipher import AES

def bytes_hex(bytes):
	return ''.join(format(x, '02x') for x in bytes)

bs = AES.block_size
key = hashlib.sha256("omgwtfbbq".encode()).digest()
plaintext = "I was lost, but now I'm found..."

# Find first cipher block from second
cbc_block_2 = 0xc1cf6db4524aac04e222853969367e0d.to_bytes(16, 'big')

ecb_cipher = AES.new(key, AES.MODE_ECB)
ecb_dec_block_2 = ecb_cipher.decrypt(cbc_block_2)

cbc_block_1 = bytearray(16)

for i in range(16):
	cbc_block_1[i] = plaintext.encode()[16 + i] ^ ecb_dec_block_2[i]


cbc_block_1 = bytes(cbc_block_1)
print("full cipher text: {}".format(bytes_hex(cbc_block_1) + bytes_hex(cbc_block_2)))

# Find iv
ecb_dec_block_1 = ecb_cipher.decrypt(cbc_block_1)

iv = bytearray(16)

for i in range(16):
	iv[i] = plaintext.encode()[i] ^ ecb_dec_block_1[i]

iv = bytes(iv).decode()

print("iv: {}".format(iv))
