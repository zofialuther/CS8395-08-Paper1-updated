import http.server
import http.dispatch
import http.html_write

def server():
    http_server(http.dispatch, [port(8080)])

def handle_root_uri():
    http_handler('/', say_goodbye, [])

def say_goodbye(_Request):
    reply_html_page([title('Howdy')], [h1('Goodbye, World!')])