def non_empty_file(file):
    if file != '.' and file != '..':
        return True
    else:
        return False

def empty_dir(Dir):
    files = directory_files(Dir)
    for file in files:
        if non_empty_file(file):
            return False
    return True