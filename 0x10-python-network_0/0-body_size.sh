#!/bin/bash
#Bash script that takes in a URL
#Send request to that URL
#Disolay the size of the body of the response

#get the size of the response in bytes
curl -s "$1" | wc -c
