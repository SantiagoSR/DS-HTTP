#!/usr/bin/env python3

from __future__ import with_statement

import contextlib

try:
        from urllib.parse import urlencode

except ImportError:
        from urllib import urlencode

try:
        from urllib.request import urlopen

except ImportError:
        from urllib.request import urlopen

from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import sys
import threading
import urllib.parse

class Handler(BaseHTTPRequestHandler):

    def _set_response(self, url):
        
        tiny_url = ""
        request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
        with contextlib.closing(urlopen(request_url)) as response:
                tiny_url = response.read().decode('utf-8 ')
       
        self.send_response(200)
        self.end_headers()
        response = tiny_url.encode('ascii')
        self.wfile.write(response)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        
        message = (threading.currentThread().getName()).encode('ascii')
        self.wfile.write(message)
        self.wfile.write(('\n').encode('ascii'))
        return
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = post_data.decode("utf_8")
        url = urllib.parse.unquote_plus(data).split('=')[1]
        self._set_response(url)
        self.wfile.write("\n POST request for {}".format(self.path).encode('utf-8'))

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


def main():
    PORT = 3000
    server = ThreadedHTTPServer(('',PORT), Handler)
    print('Server running on port ', PORT)
    server.serve_forever()

if __name__ == "__main__":
    main()
