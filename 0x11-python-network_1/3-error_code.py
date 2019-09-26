#!/usr/bin/python3
"""
This script sends an request and displays the body of the response (error)
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            fetchi = response.read()
            print(fetchi.decode('utf-8'))
    except urllib.error.HTTPError as dont:
        print("Error code: {}".format(dont.code))
