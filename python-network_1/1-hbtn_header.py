#!/usr/bin/python3
"""Takes in a URL, sends a request and displays the value of X-Request-Id"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
