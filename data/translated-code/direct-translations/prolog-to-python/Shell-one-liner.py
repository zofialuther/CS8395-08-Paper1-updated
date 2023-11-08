import subprocess

# Running the command with swipl
swipl_command = "echo 'current_prolog_flag(dialect,D), writeln(D), halt.' | swipl -q"
swipl_output = subprocess.check_output(swipl_command, shell=True).decode('utf-8').strip()
print(swipl_output)

# Running the command with yap
yap_command = "echo 'current_prolog_flag(dialect,D), writeln(D), halt.' | yap -q"
yap_output = subprocess.check_output(yap_command, shell=True).decode('utf-8').strip()
print(yap_output)