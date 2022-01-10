
###  SEND BULK REQUEST AT A SAME TIME USING GEVENT

from __future__ import print_function
import gevent
from gevent import monkey

 # patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()
import requests

# Note that we're using HTTPS, so
# this demonstrates that SSL works.
urls = [
    'https://www.google.com/',
    'https://www.apple.com/',
    'https://www.python.org/',
    "http://www.apple.com",
    "http://www.microsoft.com",
    "http://www.amazon.com", 
    "http://www.facebook.com",
]


def print_head(url):
    print('Starting %s' % url)
    data = requests.get(url)
    print(data.status_code)


jobs = [gevent.spawn(print_head, f"{_url}") for _url in urls]

gevent.wait(jobs)



