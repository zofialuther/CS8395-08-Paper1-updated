```python
import subprocess

def main():
    process = subprocess.run(["echo", "Hello World!"], stdout=subprocess.PIPE)
    subprocess.run(["lpr"], input=process.stdout, text=True)

if __name__ == "__main__":
    main()
```