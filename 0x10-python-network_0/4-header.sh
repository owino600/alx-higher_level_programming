#!/bin/bash
# Send a GET request to a given URL with a header variable.
user_id=98
curl -s -H "X-School-User-Id: $user_id" "${1}"