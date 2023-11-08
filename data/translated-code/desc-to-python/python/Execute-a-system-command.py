import subprocess

try:
    output = subprocess.check_output(['ls', '-l'])
except subprocess.CalledProcessError as e:
    print("Error: ", e)
else:
    print(output)