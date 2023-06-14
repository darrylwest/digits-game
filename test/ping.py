#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-14 17:15:17

# best to use node to test

# import argparse
import http.client

host = "piedmont:9890"

def ping():
    conn = http.client.HTTPConnection(host)
    conn.request("GET", "/")

    response = conn.getresponse()
    print(response.status, response.reason)

    if response.reason == "OK":
        body = response.read()
        print(body)

    conn.close()

def main():
    ping()

if __name__ == '__main__':
    main()
