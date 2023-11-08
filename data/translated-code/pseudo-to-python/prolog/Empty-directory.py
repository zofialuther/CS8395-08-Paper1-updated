def non_empty_file(file):
    if file == '.' or file == '..':
        return True
    else:
        return False

def empty_dir(Dir):
    Files = directory_files(Dir)
    for file in Files:
        if not non_empty_file(file):
            return False
    return True