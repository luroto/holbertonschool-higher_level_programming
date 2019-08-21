#!/bin/bash
# This script sends a POST request with some keys and values 
curl -s "$1" -X POST -d "email=hr@holbertonschool.com" -d "subject=I always be here for PLD"
