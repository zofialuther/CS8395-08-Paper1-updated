import os

directory_path = input("Enter the directory path: ")

if len(os.listdir(directory_path)) == 0:
    print("empty")
else:
    print("not empty")