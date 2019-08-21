#!/bin/bash
# This script gets the http code
curl -so /dev/null -s -w "%{http_code}" "$1"
