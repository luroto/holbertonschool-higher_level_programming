#!/bin/bash
# This script sends a POST request with some keys and values 
curl -sd "email=hr@holbertonschool.com&subject=I always be here for PLD" "$1"
