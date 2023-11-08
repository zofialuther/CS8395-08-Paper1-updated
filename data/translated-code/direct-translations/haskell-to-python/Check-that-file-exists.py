from os import path

def check(p, s):
    result = p(s)
    print(s + (" does exist" if result else " does not exist"))

def main():
    check(path.isfile, "input.txt")
    check(path.isdir, "docs")
    check(path.isfile, "/input.txt")
    check(path.isdir, "/docs")

main()