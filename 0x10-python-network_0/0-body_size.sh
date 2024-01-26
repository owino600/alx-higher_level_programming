#!/bin/bash
#get the size of the response in bytes
curl -sI "$1" | grep -i Content-Length |cut -d " " -f 2
