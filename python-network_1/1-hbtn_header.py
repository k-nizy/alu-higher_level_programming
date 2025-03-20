#!/usr/bin/python3
"""
Fetches a , sends a request, and displays the value of the X-Request-Id header.
"""
import urllib.request
import sys

if __name__ == "__main__":
    # Use a test URL that returns the X-Request-Id header
    url = "https://httpbin.org/headers"
    # Add a User-Agent header to the request
    headers = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        headers = response.info()
        x_request_id = headers.get("X-Request-Id")
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
