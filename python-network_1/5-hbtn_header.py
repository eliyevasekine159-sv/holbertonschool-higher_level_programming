#!/usr/bin/python3
"""Takes a URL, sends a request and displays the X-Request-Id header value"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
