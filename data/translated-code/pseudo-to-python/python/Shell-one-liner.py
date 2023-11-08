import CGIHTTPServer

server = CGIHTTPServer.CGIHTTPRequestHandler()
server.port = 8000
server.serve_forever()