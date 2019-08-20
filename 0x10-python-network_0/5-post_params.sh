#!/bin/bash
# This script sends a POST request with some keys and values 
curl -s -X POST -F "email=hr@holbertonschool.com" -F "subject=I always be here for PLD" "$1"
