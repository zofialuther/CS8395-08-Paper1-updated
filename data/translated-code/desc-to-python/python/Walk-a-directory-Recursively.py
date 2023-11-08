import fnmatch
import os

def print_fnmatches(pattern, directory, files):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(directory, filename))

root_directory = "/path/to/root/directory"
pattern = "*.mp3"

for directory, subdirectories, files in os.walk(root_directory):
    print_fnmatches(pattern, directory, files)