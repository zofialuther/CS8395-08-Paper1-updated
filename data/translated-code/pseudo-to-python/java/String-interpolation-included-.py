from string import Formatter
from io import StringIO

string = StringIO()
formatter = Formatter(string)
adjective = "little"
formatter.format("Mary had a {0} lamb", adjective)
print(string.getvalue())