import subprocess

exit_code = subprocess.check_call(['ls', '-l'])
assert exit_code == 0

output = subprocess.check_output(['ls', '-l'])