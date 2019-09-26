#!/usr/bin/python3
"""
This script finds X-Requested-Id of a request
"""
if __name__ == "__main__":
    import sys
    import urllib.request
    linkcito = sys.argv[1]
    req = urllib.request.Request(linkcito)
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
