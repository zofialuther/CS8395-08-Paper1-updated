import subprocess

output = subprocess.check_output(['ls'])
print(output.decode('utf-8'))