import os

def isEmptyDir(dirName):
    fileArray = os.listdir(dirName)
    return len(fileArray) == 0