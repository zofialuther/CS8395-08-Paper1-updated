import os

# Check for the existence of input.txt and docs directory in the current directory
if os.path.exists('input.txt') and os.path.isdir('docs'):
    print("File 'input.txt' and directory 'docs' exist in the current directory")

# Check for the existence of input.txt and docs directory using absolute paths
if os.path.exists('/absolute/path/to/input.txt') and os.path.isdir('/absolute/path/to/docs'):
    print("File 'input.txt' and directory 'docs' exist using absolute paths")