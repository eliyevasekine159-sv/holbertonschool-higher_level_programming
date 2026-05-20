#!/usr/bin/python3
"""Fetches status URL using urllib with dynamic argument option"""
import sys
import urllib.request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    if len(sys.argv) > 1:
        url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
