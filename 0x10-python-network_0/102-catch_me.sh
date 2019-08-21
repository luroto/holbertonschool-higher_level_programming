#!/bin/bash
# This script is for a challenge
curl -s -L -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" "$1"
