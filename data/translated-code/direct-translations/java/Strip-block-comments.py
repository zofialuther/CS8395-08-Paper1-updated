import java.io

def readFile(filename):
    with open(filename, 'r') as file:
        return file.read()

def stripComments(beginToken, endToken, input):
    output = ""
    while True:
        begin = input.find(beginToken)
        end = input.find(endToken, begin + len(beginToken))
        if begin == -1 or end == -1:
            output += input
            return output
        output += input[0:begin]
        input = input[end + len(endToken):]

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage: BeginToken EndToken FileToProcess")
        sys.exit(1)

    begin = sys.argv[1]
    end = sys.argv[2]
    input_file = sys.argv[3]

    try:
        print(stripComments(begin, end, readFile(input_file)))
    except Exception as e:
        print(e)
        sys.exit(1)