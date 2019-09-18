#!/usr/bin/python3
"""
This script sends an request and displays the body of the response (error)
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    req = requests.get(url)
    try:
        req.raise_for_status()
    except:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
