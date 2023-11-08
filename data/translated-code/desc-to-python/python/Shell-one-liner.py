from http.server import CGIHTTPRequestHandler, HTTPServer

port = 8000
server_address = ("", port)

httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
print(f"Starting CGI server on port {port}")
httpd.serve_forever()