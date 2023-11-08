import os

def find_common_prefix(file_paths):
    return os.path.commonpath(file_paths)

file_paths = ['/home/user1/tmp/cove/file1.txt', '/home/user1/tmp/cove/file2.txt', '/home/user1/tmp/cove/file3.txt']
common_prefix = find_common_prefix(file_paths)
print(common_prefix)