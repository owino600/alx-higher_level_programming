#!/bin/bash
# script that sends request to URL
curl -s -L -X HEAD -w "%{http_code}" "$1"
