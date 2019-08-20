#!/bin/bash
# This script sends a POST request with some keys and values 
curl -s --data "email=hr@holbertonschool.com&subject=I always be here for PLD" "$1"
