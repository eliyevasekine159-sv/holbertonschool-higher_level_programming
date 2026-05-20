#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request with the email as parameter"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Parametri lüğət şəklində hazırlayırıq və urlencode ilə kodlaşdırırıq
    values = {'email': email}
    data = urllib.parse.urlencode(values).encode('utf-8')
    
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
