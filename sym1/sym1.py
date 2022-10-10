#!/bin/env python3

import base64
import hashlib

# pip install pycrypto
from Crypto.Cipher import AES

# plaintext = "I was lost, but ________________"
plaintext = "I was lost, but now I'm found..."

bs = AES.block_size
key = hashlib.sha256("omgwtfbbq".encode()).digest()
iv = "________________".encode()

cipher = AES.new(key, AES.MODE_CBC, iv)

ciphertext = cipher.encrypt(plaintext.encode())

print(''.join(format(x, '02x') for x in ciphertext))

# __f374a82db50b23_____b88f1d976ddc1cf6db4524aac04e222853969367e0d
