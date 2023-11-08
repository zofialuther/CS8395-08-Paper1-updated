def test_run():
    proc_dir('C:\\vvvv\\vvvv_beta_39_x64')

def proc_dir(Directory):
    print("Directory: " + Directory)
    Files = directory_files(Directory)
    proc_files(Directory, Files)

def proc_files(Directory, Files):
    for File in Files:
        proc_file(Directory, File)
    proc_files(Directory, [])

def proc_file(Directory, File):
    if File == '.' or File == '..' or exists_directory(directory_file_path(Directory, File, Path)):
        print("Directory: " + File)
    elif exists_file(directory_file_path(Directory, File, Path)):
        print("File: " + File)
    else:
        print("Unknown: " + File)