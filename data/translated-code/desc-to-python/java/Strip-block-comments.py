```python
class StripBlockComments:
    
    def __init__(self):
        pass
    
    def readFile(self, filename):
        try:
            with open(filename, 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            print("File not found")
            return ""
    
    def stripComments(self, data, begin_token, end_token):
        start = data.find(begin_token)
        while start != -1:
            end = data.find(end_token, start + len(begin_token))
            if end == -1:
                end = len(data)
            data = data[:start] + data[end + len(end_token):]
            start = data.find(begin_token)
        return data
    
    def main(self, begin_token, end_token, filename):
        file_data = self.readFile(filename)
        if file_data:
            stripped_data = self.stripComments(file_data, begin_token, end_token)
            print(stripped_data)
        else:
            print("Error reading file")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python StripBlockComments.py <begin_token> <end_token> <filename>")
    else:
        begin_token = sys.argv[1]
        end_token = sys.argv[2]
        filename = sys.argv[3]
        sbc = StripBlockComments()
        sbc.main(begin_token, end_token, filename)
```