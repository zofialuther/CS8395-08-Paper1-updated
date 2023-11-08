from pathlib import Path

file_path = Path("`Abdu'l-Bah\u00E1.txt")
if file_path.exists():
    print("File exists")
else:
    print("File does not exist")