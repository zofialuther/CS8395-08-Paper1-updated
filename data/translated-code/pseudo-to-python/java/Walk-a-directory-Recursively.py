import os

def walkin(directory):
    pattern = ".mp3"
    listFile = os.listdir(directory)
    if listFile is not None:
        for file in listFile:
            if os.path.isdir(os.path.join(directory, file)):
                walkin(os.path.join(directory, file))
            else:
                if file.endswith(pattern):
                    print(os.path.join(directory, file))

def main():
    walkin("/home/user")