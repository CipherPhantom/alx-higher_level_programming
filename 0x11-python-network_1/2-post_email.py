#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    values = {
            "email": sys.argv[2]
            }
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
