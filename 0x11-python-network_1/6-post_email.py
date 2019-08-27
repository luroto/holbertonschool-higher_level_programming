#!/usr/bin/python3
"""
This script sends a POST request to some URL
"""
if __name__ == "__main__":
    import sys
    import requests
    linkcito = sys.argv[1]
    email = sys.argv[2]
    valores = {'email': email}
    req = requests.post(linkcito, data=valores)
    print(req.text)
