from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import requests

class statusHandler(BaseHTTPRequestHandler):
    def _set_response(self, url):
        #Gets the status of the requested page
        url_status = requests.get(url).status_code
        self.send_response(url_status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello Cono!'.encode())

    def do_POST(self):
        r = requests.post("http://ec2-54-165-183-13.compute-1.amazonaws.com:3000                                                                                                                                                             ")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        #Decodes passed info
        received_string = post_data.decode('utf_8')
        #Parses URL encode to regular string and splits the passed string by =
        url = urllib.parse.unquote_plus(received_string).split('=')[1]
        self._set_response(url)
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8')                                                                                                                                                             )


def main():
     PORT = 3000
     server = HTTPServer(('', PORT), statusHandler)
     print('Server running on port %s ' % PORT)
     server.serve_forever()

if __name__== '__main__':
    main()
