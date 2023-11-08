import http.server
import sys

port = 8000
if len(sys.argv) > 1:
    port = int(sys.argv[1])

http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler, port=port)