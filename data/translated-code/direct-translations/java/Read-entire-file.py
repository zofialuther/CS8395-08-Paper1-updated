from pathlib import Path
import charset

def read_all_lines(filename):
    file = Path(filename)
    return file.read_text()

def read_all_bytes(filename):
    file = Path(filename)
    return file.read_bytes()