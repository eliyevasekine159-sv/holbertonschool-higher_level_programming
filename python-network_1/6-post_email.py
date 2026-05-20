#!/usr/bin/python3
"""Takes a URL and an email, sends a POST request using requests package"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}

    r = requests.post(url, data=payload)
    print(r.text)
