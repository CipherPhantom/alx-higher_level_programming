#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == "__main__":

    url = "https://api.github.com/user"
    session = requests.Session()
    session.auth = (sys.argv[1], sys.argv[2])
    response = session.get(url)
    if "id" in response.json():
        print(response.json()["id"])
    else:
        print("None")
