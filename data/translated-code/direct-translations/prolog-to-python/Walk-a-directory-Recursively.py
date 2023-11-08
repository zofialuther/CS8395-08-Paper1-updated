```python
import os

def test_run():
    proc_dir('C:\\vvvv\\vvvv_beta_39_x64')

def proc_dir(Directory):
    print(f'Directory: {Directory}')
    files = os.listdir(Directory)
    proc_files(Directory, files)

def proc_files(Directory, files):
    for file in files:
        proc_file(Directory, file)

def proc_file(Directory, file):
    path = os.path.join(Directory, file)
    if file == '.' or file == '..':
        if os.path.isdir(path):
            print(f'Directory: {file}')
    else:
        if os.path.isdir(path):
            proc_dir(path)
        elif os.path.isfile(path):
            print(f'File: {file}')
        else:
            print(f'Unknown: {file}')
```