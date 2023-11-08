import sys

def process_input(input_line):
    result = input_line.split(';#')[0]
    print(result)

if __name__ == "__main__":
    input_lines = sys.stdin.readlines()
    map(process_input, input_lines)