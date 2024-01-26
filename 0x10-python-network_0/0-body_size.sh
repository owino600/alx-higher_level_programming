#!/bin/bash
#Bash script that takes in a URL
#Send request to that URL
#Disolay the size of the body of the response

#get the size of the response in bytes
curl -sI "$1" | grep -i Content-Length |cut -d " " -f 2
