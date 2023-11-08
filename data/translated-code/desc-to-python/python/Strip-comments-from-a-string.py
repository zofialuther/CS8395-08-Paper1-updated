import itertools

def stripComments(commentChars):
    def inner(text):
        lines = text.split('\n')
        result = []
        for line in lines:
            line = line.strip()
            if not line.startswith(commentChars):
                result.append(line)
        return '\n'.join(result)
    return inner

text = """This is a multi-line
string with ; comments
# in it"""

strip = stripComments(';#')
stripped_text = strip(text)
print(stripped_text)