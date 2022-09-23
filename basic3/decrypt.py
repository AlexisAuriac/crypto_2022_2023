#!/bin/env python3

def get_header(file_bytes):
	file_size = len(file_bytes).to_bytes(4, 'little')
	return b'BM' + file_size


def get_key(file_bytes):
	header = get_header(file_bytes)

	size_key = len(header)
	key = bytearray(size_key)

	for i in range(size_key):
		key[i] = file_bytes[i] ^ header[i]

	return bytes(key)


def decrypt_file(file_bytes, key):
	size_key = len(key)
	size = len(file_bytes)
	decrypted = bytearray(len(file_bytes))

	for i in range(size):
		decrypted[i] = file_bytes[i] ^ key[i % size_key]

	return decrypted


def main():
	enc = bytearray(open('ch2.bmp', 'rb').read())

	key = get_key(enc)
	print("key: %s" % hex(int.from_bytes(key, 'big')))
	decrypted = decrypt_file(enc, key)

	open('res.bmp', 'wb').write(decrypted)


if __name__ == '__main__':
	main()
