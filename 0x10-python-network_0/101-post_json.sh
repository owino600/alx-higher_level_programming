#!/bin/bash
# script that sends a JSON POST to a URL
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
