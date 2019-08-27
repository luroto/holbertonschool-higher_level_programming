#!/usr/bin/python3
"""
This script finds X-Requested-Id of a request
"""
if __name__ == "__main__":
    import sys
    import requests
    linkcito = sys.argv[1]
    req = requests.get(linkcito)
    print(req.headers.get('X-Request-Id'))
