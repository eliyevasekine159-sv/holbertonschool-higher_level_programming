#!/usr/bin/python3
"""Takes in a URL, sends a request, and manages HTTPError exceptions"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
