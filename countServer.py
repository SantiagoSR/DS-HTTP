from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

REQUEST_COUNT = 0

class countHandler(BaseHTTPRequestHandler):

    def _set_response(self):
        #Returns the request count
        global REQUEST_COUNT
        with contextlib.closing(urlopen(REQUEST_COUNT)) as response:
                tiny_url = response.read().decode('utf-8 ')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global REQUEST_COUNT
        REQUEST_COUNT +=1
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str(REQUEST_COUNT).encode('ascii'))

    def do_POST(self):
        global REQUEST_COUNT
        REQUEST_COUNT += 1
        #content_length = int(self.headers['Content-Length'])
        #post_data = self.rfile.read(content_length)
        #Decodes passed info
        #received_string = post_data.decode('utf_8')
        #Parses URL encode to regular string and splits the passed string by =
        #url = urllib.parse.unquote_plus(received_string).split('=')[1]
        self._set_response()
        print(f"!!!!!!!!!!!!!REQUEST_COUNT {REQUEST_COUNT}!!!!!!!!!!!!!!!!!!")
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8')                                                                                                             )


def main():

     PORT = 3000
     server = HTTPServer(('', PORT), countHandler)
     print('Server running on port %s ' % PORT)
     server.serve_forever()

if __name__== '__main__':
    main()
