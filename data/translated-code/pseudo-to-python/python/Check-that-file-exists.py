import os

if os.path.isfile("input.txt"):
    print("input.txt is a file")
else:
    print("input.txt is not a file")

if os.path.isfile("/input.txt"):
    print("/input.txt is a file")
else:
    print("/input.txt is not a file")

if os.path.isdir("docs"):
    print("docs is a directory")
else:
    print("docs is not a directory")

if os.path.isdir("/docs"):
    print("/docs is a directory")
else:
    print("/docs is not a directory")