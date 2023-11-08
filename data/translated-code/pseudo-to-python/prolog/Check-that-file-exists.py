def exists_file(file_path):
    if file_path.startswith('/'):
        print("File exists in root directory")
    else:
        print("File exists in current directory")

def exists_directory(directory_path):
    if directory_path.startswith('/'):
        print("Directory exists in root directory")
    else:
        print("Directory exists in current directory")

exists_file('input.txt')
exists_directory('docs')

exists_file('/input.txt')
exists_directory('/docs')