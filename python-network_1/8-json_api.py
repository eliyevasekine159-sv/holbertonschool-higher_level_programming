#!/usr/bin/python3
"""Takes in a letter and sends a POST request to a search API"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    payload = {'q': q}
    url = "http://0.0.0.0:5000/search_user"

    try:
        r = requests.post(url, data=payload)
        response_json = r.json()

        if not response_json:
            print("No result")
        else:
            print("[{}] {}".format(response_json.get('id'),
                                   response_json.get('name')))
    except ValueError:
        print("Not a valid JSON")
