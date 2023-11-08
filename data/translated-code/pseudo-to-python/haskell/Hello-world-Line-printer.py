import subprocess

def main():
    subprocess.run(["echo", "Hello World! | lpr"], shell=True, check=True)