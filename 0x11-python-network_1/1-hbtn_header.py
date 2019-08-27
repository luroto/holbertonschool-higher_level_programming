#!/usr/bin/python3
"""
This script finds X-Requested-Id of a request
"""
import sys
import urllib.request
linkcito = sys.argv[1]
req = urllib.request.Request(linkcito)
with urllib.request.urlopen(req) as response:
    fetching = response.read()
dicto = dict(response.getheaders())
print(dicto['X-Request-Id'])
