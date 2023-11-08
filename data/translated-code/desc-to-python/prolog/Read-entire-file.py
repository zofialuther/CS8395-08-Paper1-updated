import sys
from pyswip import Prolog

prolog = Prolog()

file_name = sys.argv[1]
content = list(prolog.query(f'read_file_to_string("{file_name}", Content)'))
print(content[0]['Content'])