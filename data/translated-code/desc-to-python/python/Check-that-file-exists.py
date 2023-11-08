import os

file_exists_in_cwd = os.path.isfile("input.txt")
dir_exists_in_cwd = os.path.isdir("docs")

file_exists_in_root = os.path.isfile("/input.txt")
dir_exists_in_root = os.path.isdir("/docs")