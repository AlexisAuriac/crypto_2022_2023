#!/bin/env python3

import sys

def main(hex_str):
	print(bytes.fromhex(hex_str).decode('utf-8'))

if __name__ == '__main__':
	main(sys.argv[1])
