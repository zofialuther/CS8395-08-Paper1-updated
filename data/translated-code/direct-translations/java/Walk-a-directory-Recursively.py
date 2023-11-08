from os import listdir
from os.path import isfile, join

def walkin(dir):
    pattern = ".mp3"
    files = [f for f in listdir(dir) if isfile(join(dir, f))]
    for file in files:
        if file.endswith(pattern):
            print(join(dir, file))

walkin("/home/user") #Replace this with a suitable directory