#!/bin/bash
# This script lists all the available methods
curl -s -i -X OPTIONS "$1" | grep Allow: | cut -d" "  -f 2-6 
