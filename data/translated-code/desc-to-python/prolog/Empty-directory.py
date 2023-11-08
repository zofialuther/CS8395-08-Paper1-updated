from os import listdir
from os.path import isfile, getsize

def non_empty_file(file):
    return file != '.' and file != '..' and getsize(file) > 0

def empty_dir(directory):
    files = [f for f in listdir(directory) if isfile(f)]
    return all(map(non_empty_file, files))