import sys

def main():
    Arguments = sys.argv
    File = get_first_argument(Arguments)
    with open(File, 'r') as file:
        String = file.read()

def get_first_argument(arguments):
    return arguments[1]

if __name__ == "__main__":
    main()