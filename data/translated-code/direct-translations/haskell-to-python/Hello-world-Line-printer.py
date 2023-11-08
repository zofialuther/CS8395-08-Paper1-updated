from subprocess import Popen, PIPE

def main():
    process = Popen('echo "Hello World!" | lpr', shell=True, stdout=PIPE, stderr=PIPE)
    return process

if __name__ == "__main__":
    main()