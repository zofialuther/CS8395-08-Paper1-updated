import sys

def main():
    file = sys.argv[1]
    with open(file, 'r') as f:
        string = f.read()
        print(string)

if __name__ == "__main__":
    main()