from pyswip import Prolog
from pyswip.easy import registerForeign

prolog = Prolog()

def handler(request):
    if request['path'] == '/':
        return {
            'status': 200,
            'headers': [('Content-Type', 'text/html')],
            'body': '<html><head><title>Howdy</title></head><body><h1>Goodbye, World!</h1></body></html>'
        }
    else:
        return {
            'status': 404,
            'headers': [('Content-Type', 'text/plain')],
            'body': 'Not Found'
        }

registerForeign(handler, arity=1)
prolog.consult("server.pl")
prolog.assertz("server(8080)")
prolog.assertz("handler(/, handle_request)")