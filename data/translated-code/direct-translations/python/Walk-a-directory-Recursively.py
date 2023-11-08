import fnmatch
import os

def print_fnmatches(arg, dir, files):
    pattern = arg
    for filename in files:
        if fnmatch.fnmatch(filename, pattern):
            print(os.path.join(dir, filename))

os.path.walk('/', print_fnmatches, '*.mp3')