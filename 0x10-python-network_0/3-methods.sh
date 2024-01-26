#!/bin/bash
# Display all HTTP methods the server
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
