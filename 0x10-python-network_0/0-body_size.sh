#!/bin/bash
#Bash script that takes in a URL
#Send request to that URL
#Disolay the size of the body of the response

if [$"#" -eq 0]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

#send request to the url
URL=$1
response=$(curl -s "$URL")

#get the size of the response in bytes

curl -s "response" | wc -c