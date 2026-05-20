#!/usr/bin/python3
"""Takes GitHub credentials and uses the GitHub API to display the user id"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=(username, token))
    try:
        response_json = r.json()
        print(response_json.get('id'))
    except ValueError:
        print("None")
