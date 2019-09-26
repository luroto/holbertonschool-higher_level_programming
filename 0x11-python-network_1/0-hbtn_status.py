#!/usr/bin/python3
""" This task is for exploring bytes methods and dict"""
if __name__ == __main__:
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        fetching = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(fetching)))
    print("\t- content: {}".format(fetching))
    print("\t- utf8 content: {}".format(fetching.decode('utf-8')))
