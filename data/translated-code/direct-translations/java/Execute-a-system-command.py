```python
import subprocess

def executeCmd(command):
    try:
        aProcess = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        aProcess.wait()

        pipedOut = aProcess.stdout
        buffer = bytearray(2048)
        read = pipedOut.readinto(buffer)
        # Replace following code with your intends processing tools
        while read >= 0:
            print(buffer.decode('utf-8'), end='')
            read = pipedOut.readinto(buffer)
    except subprocess.CalledProcessError as e:
        print(e.output.decode('utf-8'))
    finally:
        if pipedOut:
            pipedOut.close()

if __name__ == "__main__":
    executeCmd("ls -oa")
```