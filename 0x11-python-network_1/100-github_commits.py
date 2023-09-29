#!/usr/bin/python3
"""
This script list 10 commits.
It takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
"""
import sys
import requests

if __name__ == "__main__":
    url = "  https://api.github.com/repos/{}/{}/commits"
    response = requests.get(url.format(sys.argv[1], sys.argv[2]))
    count = 0
    for commit in response.json():
        if count == 10:
            break
        info = "{}: {}"
        print(info.format(commit["sha"], commit["commit"]["author"]["name"]))
        count += 1
