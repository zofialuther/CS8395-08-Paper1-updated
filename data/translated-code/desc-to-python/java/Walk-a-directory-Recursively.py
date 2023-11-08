```python
import os

class MainEntry:
    @staticmethod
    def main():
        directory = "/path/to/directory"
        MainEntry.walkin(directory)

    @staticmethod
    def walkin(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".mp3"):
                    print(os.path.join(root, file))
```