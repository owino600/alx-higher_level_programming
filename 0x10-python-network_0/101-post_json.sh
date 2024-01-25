#!/bin/bash
# script that sends a JSON POSTrequest to a URL passedas the first argument

curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"