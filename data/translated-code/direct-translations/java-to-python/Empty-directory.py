from pathlib import Path

def isEmptyDir(dirName):
    return len(list(Path(dirName).iterdir())) == 0