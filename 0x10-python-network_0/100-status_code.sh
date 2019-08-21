#!/bin/bash
# This script gets the http code
curl -o /dev/null -s -w "%{http_code}\n" "$1"

