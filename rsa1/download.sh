#!/bin/bash

site="https://crypto.geographer.fr"
file1="rsa1.pem"
file2="rsa1Cipher.txt"

url1="$site/$file1"
url2="$site/$file2"

curl "$url1" > "$file1"
curl "$url2" > "$file2"
