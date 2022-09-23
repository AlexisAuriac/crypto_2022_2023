#!/bin/bash

site="https://crypto.geographer.fr"
file="ch2.bmp"

url="$site/$file"

curl "$url" > "$file"
