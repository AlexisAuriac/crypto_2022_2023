#!/bin/bash

site="https://crypto.geographer.fr"
file="ch3.jpg"

url="$site/$file"

curl "$url" > "$file"
