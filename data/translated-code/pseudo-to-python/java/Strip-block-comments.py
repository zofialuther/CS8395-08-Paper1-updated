def readFile(filename):
    with open(filename, 'r') as file:
        fileContents = file.read()
    return fileContents

def stripComments(beginToken, endToken, input):
    output = ""
    while True:
        begin = input.find(beginToken)
        end = input.find(endToken, begin + len(beginToken))
        if begin == -1 or end == -1:
            output += input
            return output
        output += input[:begin]
        input = input[end + len(endToken):]

def main(args):
    if len(args) < 3:
        print("Usage: BeginToken EndToken FileToProcess")
        exit(1)
    begin = args[0]
    end = args[1]
    input_file = args[2]
    try:
        print(stripComments(begin, end, readFile(input_file)))
    except Exception as e:
        print(e)
        exit(1)