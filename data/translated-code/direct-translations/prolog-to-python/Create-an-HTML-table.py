from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Data received: ".encode())
        self.wfile.write(form.getvalue("data").encode())

def main():
    try:
        server = HTTPServer(('', 8080), MyHandler)
        print('Server started on http://localhost:8080')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()

if __name__ == '__main__':
    main()