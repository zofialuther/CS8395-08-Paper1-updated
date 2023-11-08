def check(p, s):
    result = p(s)
    print(s + " " + ("does exist" if result else "does not exist"))

def main():
    check(os.path.isfile, "input.txt")
    check(os.path.isdir, "docs")
    check(os.path.isfile, "/input.txt")
    check(os.path.isdir, "/docs")