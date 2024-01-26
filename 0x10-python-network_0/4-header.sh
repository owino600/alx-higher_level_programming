#!/bin/bash
# Send a GET request to a given URL
user_id=98
curl -s "$1" -H "X-School-User-Id: $user_id" 
