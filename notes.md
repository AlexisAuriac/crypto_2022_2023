# Step 1

todo: make a script for it

### first try

3 - ctlf.rpobakotiy.coo

rail fence -> crypto.blackfoot.io

### second try

3 - ctearrpogorpe.ry.ghf

rail fence -> crypt.geographer.fr

# Step 2

curl https://crypto.geographer.fr/ > step2.txt

Encrypted with monoalphabetic substitution

     ABCDEFGHIJKLMNOPQRSTUVWXYZ
     DPEJRFLMSNKIHUXZGQTVWCBAYO
key: XWVACFQMLDKGHJZBREISNTUOYP

don't need to find the key again, need to make script to decrypt though

# Exercises

## Basic

### Basic 2

todo: make script

data: 57656c6c20646f6e6520212054686520666c616720666f722074686973206368616c6c656e67652069732074686973206d6573736167652e
base: hex https://www.convertstring.com/EncodeDecode/HexDecode
flag: Well done ! The flag for this challenge is this message.

### Basic 3

download file: ```wget https://crypto.geographer.fr/ch2.bmp```
xor encrypted file

Solution:\
source: https://en.wikipedia.org/wiki/BMP_file_format
We know part of the file header: type (0x424D 'BM') and file size\
data ^ key = encrypted <=> encrypted ^ data = key

Result:\
key: 0x676974677564\
flag: 'Bravo les loulous'

### Basic 4

download file: ```wget https://crypto.geographer.fr/basic4.webp```
xor encoded file
source: https://developers.google.com/speed/webp/docs/riff_container#webp_file_header

same as Basic 3
header is: riff (0x52494646 'RIFF') + file_size-8 + webp (0x57454250 'WEBP') + VP8 (0x565038 'VP8')

## hash

### Easy hashing

todo: make script for it

37f62f1363b04df4370753037853fe88
https://hashes.com/en/decrypt/hash
trololo

### Confessions

todo: cleanup/improve current script

Endpoint request logs:\
```
https://confessions.geographer.fr/graphql?query={requestsLog%20{name,%20args,%20timestamp}}
```
