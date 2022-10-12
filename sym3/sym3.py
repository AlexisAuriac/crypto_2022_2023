#!/bin/env python3

# https://github.com/JeffersonDing/CTF/blob/master/pico_CTF_2021/web/more_cookies/ape.py
# https://dr3dd.gitlab.io/cryptography/2019/01/10/simple-AES-CBC-bit-flipping-attack/

import requests
import threading
import re
from base64 import b64decode
from base64 import b64encode

url = 'http://flip2.geographer.fr/'

s = requests.Session()
blockSize = 16

def getInitCookie(s):
    response = s.post(url + 'login', data={'user': '', 'password': ''})
    initCookieBase64 = s.cookies['cookie']

    initCookie = b64decode(initCookieBase64)
    iv = initCookie[:16]
    enc = initCookie[16:]

    return iv, enc

iv, enc = getInitCookie(s)

print('inital iv: ', iv)
print('inital enc: ', enc)

def cutUsernameAndPassword(s, iv, enc):
    iv = enc[-32:-16]
    enc = enc[-16:]

    for i in range(1, 256):
        newIv = bytearray(iv)
        newIv[0] = newIv[0] ^ i
        newIv = bytes(newIv)

        newcookie = b64encode(newIv + enc).decode()
        cookies_dict = {'cookie': newcookie}
        response = requests.get(url + 'flag', cookies=cookies_dict)
        html = response.content.decode()
        match = re.search(r'Cookie', html)

        if match is not None:
            return newIv, enc

iv, enc = cutUsernameAndPassword(s, iv, enc)

found = False
correctCookie = ''
flag = ''

def bitFlip(byte, bit):
    mask = 2 ** bit

    newIv = bytearray(iv)
    newIv[byte] = newIv[byte] ^ mask
    return bytes(newIv)

def testCookie(i):
    global found
    global correctCookie
    global flag

    for j in range(8):
        if found:
            exit()
        newIv = bitFlip(i, j)
        newcookie = b64encode(newIv + enc).decode()

        cookies_dict = {'cookie': newcookie}
        response = requests.get(url + 'flag', cookies=cookies_dict)
        html = response.content.decode()

        match = re.search(r'BFS\{.+\}', html)

        if match is not None:
            found = True
            correctCookie = newcookie
            flag = match.group(0)


threads = []

for i in range(0, blockSize):
    t = threading.Thread(target=testCookie, args=[i])
    t.daemon = True
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    try:
        thread.join()
    except:
        continue

if found:
    print('Admin cookie: ' + correctCookie)
    print('Flag: ' + flag)
else:
    print('Not found')
    exit(1)
