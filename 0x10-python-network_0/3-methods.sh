#!/bin/bash
# Display all HTTP methods
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
