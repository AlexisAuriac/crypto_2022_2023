#!/bin/bash

curl 'https://confessions.geographer.fr/graphql?query=\{requestsLog\{name,args,timestamp\}\}' > logs.json
