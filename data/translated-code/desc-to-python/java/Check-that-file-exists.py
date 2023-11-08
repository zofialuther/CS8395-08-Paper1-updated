import os

file_name = "Abdu'l-Bah\u00E1.txt"
if os.path.exists(file_name):
    print("File exists")
else:
    print("File does not exist")