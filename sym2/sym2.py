# https://github.com/JeffersonDing/CTF/blob/master/pico_CTF_2021/web/more_cookies/ape.py
# https://dr3dd.gitlab.io/cryptography/2019/01/10/simple-AES-CBC-bit-flipping-attack/

import requests
import threading
import re
from base64 import b64decode
from base64 import b64encode

initCookieBase64 = "Q01pZXV4VW5JVlJhbmRvbbBNVUWTyb3i9ih6TPY9OvoHfMDks0jYZxXjVhA1JFKOw0qUn7dEU7gUE+1sGHAZwAHxxAm7InQXMEbchbSKHOg="
initCookie = b64decode(initCookieBase64)
iv = initCookie[:16]
enc = initCookie[-64:]
ivSize = 16

print(iv)

s = requests.Session()
url = "http://flip1.geographer.fr/flag"
print("Starting enumeration on {}".format(url))

# todo: get init cookie from http://flip1.geographer.fr/login
# response = s.get(url, cookies={'cookie': initCookieBase64}, stream=True)
# cookie = s.cookies['auth_name']

print("initial cookie: {}".format(initCookieBase64))
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
        response = requests.get(url, cookies=cookies_dict)
        html = response.content.decode()

        match = re.search(r'BFS\{.+\}', html)

        if match is not None:
            found = True
            correctCookie = newcookie
            flag = match.group(0)


threads = []

for i in range(0, ivSize):
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

print("Correct cookie: " + correctCookie)
print("Flag: " + flag)
