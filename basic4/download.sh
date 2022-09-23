#!/bin/bash

site="https://crypto.geographer.fr"
file="basic4.webp"

url="$site/$file"

curl "$url" > "$file"
