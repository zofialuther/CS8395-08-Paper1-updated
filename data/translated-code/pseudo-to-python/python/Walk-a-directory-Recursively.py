import fnmatch
import os
import os.path

def print_fnmatches(pattern, dir, files):
    for filename in files:
        if fnmatch.fnmatch(filename, pattern):
            print(os.path.join(dir, filename))

os.path.walk('/', print_fnmatches, '*.mp3')