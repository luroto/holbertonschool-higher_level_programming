#!/usr/bin/python3
"""
This script sends a POST request to some URL
"""
if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse
    linkcito = sys.argv[1]
    email = sys.argv[2]
    valores = {'email': email}
    data = urllib.parse.urlencode(valores)
    data = data.encode('ascii')
    req = urllib.request.Request(linkcito, data)
    with urllib.request.urlopen(req) as response:
        catching = response.read()
        print(catching.decode('utf-8'))
