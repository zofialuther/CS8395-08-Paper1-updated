```python
import http.server
import socketserver
import threading

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write("Hello World! 今日は".encode('utf-8'))

def serve(server_class=socketserver.ThreadingTCPServer, handler_class=MyHttpRequestHandler):
    server_address = ('', 80)
    httpd = server_class(server_address, handler_class)
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        httpd.shutdown()

serve()
```