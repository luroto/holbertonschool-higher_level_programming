#!/usr/bin/python3
"""
This script sends an request and displays the body of the response (error)
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    try:
        req = requests.get(url)
        print(req.text)
    except HTTPError as dont:
        print("Error code: {}".format(dont.response.status_code))
