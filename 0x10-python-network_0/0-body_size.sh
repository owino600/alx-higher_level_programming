#!/bin/bash
#Bash script that takes in a URL
#Send request to that URL
#Disolay the size of the body of the response
#send request to the url

URL=$1
response=$(curl -s "$URL")
#get the size of the response in bytes
curl -s "$response" | wc -c
