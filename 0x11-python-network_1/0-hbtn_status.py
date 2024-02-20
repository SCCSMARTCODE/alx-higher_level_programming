#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
from urllib import request

req = request.Request('https://alx-intranet.hbtn.io/status')
with request.urlopen(req) as response:
    the_page = response.read()
    print("Body response:")
    print("\t- type:", type(the_page))
    print("\t- content:", the_page)
    print("\t- utf8 content:", the_page.decode("utf-8"))

