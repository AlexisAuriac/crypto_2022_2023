# Get website

3 - ctearrpogorpe.ry.ghf

rail fence (3 rows) -> crypt.geographer.fr

decode: https://www.dcode.fr/rail-fence-cipher
	-> use 'Keep punctuation and spaces' option
	-> rows: 3
	-> offset: 0

script: ```node railFence.js ctearrpogorpe.ry.ghf 3```

# Exercises

## Basic 1

url: https://crypto.geographer.fr/

Encrypted with monoalphabetic substitution

used https://www.dcode.fr/monoalphabetic-substitution to get key
There were some errors that had to be corrected manually

     ABCDEFGHIJKLMNOPQRSTUVWXYZ
key: XWVACFZMLDKGHJQBREISNTUOYP

key doesn't change

use updateSubject.js to update the subject (downloads and decrypts automatically)

### Basic 2

data: 57656c6c20646f6e6520212054686520666c616720666f722074686973206368616c6c656e67652069732074686973206d6573736167652e

```
./basic2.py 57656c6c20646f6e6520212054686520666c616720666f722074686973206368616c6c656e67652069732074686973206d6573736167652e
```

web: hex https://www.convertstring.com/EncodeDecode/HexDecode
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
md5
https://hashes.com/en/decrypt/hash
trololo

### Confessions

Endpoint request logs:\
```
https://confessions.geographer.fr/graphql?query={requestsLog%20{name,%20args,%20timestamp}}
```

## Symmetric

### Sym 1

https://crypto.stackexchange.com/questions/76512/given-the-key-the-plain-text-and-the-cipher-text-can-i-calculate-the-iv-used-in
NO BRUTEFORCE NEEDED

AES ECB mode (block by block):
```
Encryption:
CipherBlockN = Encryption(PlainBlockN, key)

Decryption:
PlainBlockN = Decryption(CipherBlockN, key)
```

AES CBC mode:
```
Encryption
CipherBlockN = Encryption(PlainBlockN ^ PlainBlockN-1, key)
and
CipherBlock0 = Encryption(PlainBlock0 ^ iv, key)

Decryption:
PlainBlockN = Decryption(CipherBlockN, key) ^ CipherBlockN-1
and
PlainBlock0 = Decryption(CipherBlock0, key) ^ iv
```

We know PlainBlock0, key and CipherBlock1.

We are searching for PlainBlock1, CipherBlock0 and iv.

PlainBlock1 can be guessed from PlainBlock0.

CipherText0:
```
    PlainBlock1 = Decryption(CipherBlock1, key) ^ CipherBlock0
<=> CipherBlock0 = Decryption(CipherBlock1, key) ^ PlainBlock1
```

iv (same principle):
```
    PlainBlock0 = Decryption(CipherBlock0, key) ^ iv
<=> iv = Decryption(CipherBlock0, key) ^ PlainBlock0
```

### Sym 2

http://flip1.geographer.fr/login -> send user and password to get cookie
http://flip1.geographer.fr/flag -> can get flag if cookie says you are admin

strat 1: flip 1 bit in cookie to change boolean and make admin\
* get base cookie
* make new cookie, try get flag, repeat

format cookie:
* base64 encoded
* once decoded:
	* part 1: iv (16 bytes)
	* part 2: aes (64 bytes)

strat 2: get iv and cipher text from cookie and guess the plain text, use that to get the key
* get base cookie
* get iv and cipher text
* guess plain text
* cipher = plain ^ key ^ iv <=> key = cipher ^ plain ^ iv
* use key to make admin cookie and get flag

https://ctftime.org/task/15305
https://github.com/JeffersonDing/CTF/blob/master/pico_CTF_2021/web/more_cookies/ape.py

strat 1 was the right one but what needed to be flipped was the IV not the ciphertext

### Sym 3

Bit flipping: https://crypto.stackexchange.com/a/66086

possible solution: https://crypto.stackexchange.com/a/76249
problem: need original plaintext + modified plain text

solution: modify plain text v3

##### Brute force

ok to break block if contains username/password value, just needs to be utf-8

probability random byte is valid utf-8:
https://math.stackexchange.com/a/751707
16 bytes:
0.87739479563671 * 0.56471777839234 ** 16
= 0.00009386386216848918
= 9.39e-5
= 1 / 10653

##### modify plain text

**if server doesn't actually require username/password**

modify only first block

v1:
```{"password": "", "username": "aaaaaaaaaaaaaaaaaaaa", "admin": 0}```

```{"admin":1,"a":0, "username": "aaaaaaaaaaaaaaaaaaaa", "admin": 0}```

problem: json only takes last value
```
$ echo '{"a": 0, "a": 1}' | jq .
{
  "a": 1
}
```

v2
write admin on password field, cut other blocks
```{"password": "", "username": "aaaaaaaaaaaaaaaaaaaa", "admin": 0}```
into
```{"admin": 1    }```

v3 **SOLUTION**
cut all blocks but admin
second to last block as iv
```{"password": "", "username": "aaaaaaaaaaaaaaaaaaaa", "admin": 0}```
into
```{"admin": 0}```
then modify first block
```{"admin": 1}```
