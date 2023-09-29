#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if "X-Request-Id" in response.headers:
        print(response.headers["X-Request-Id"])
