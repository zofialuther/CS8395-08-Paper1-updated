import subprocess

input_string = "current_prolog_flag(dialect,D), writeln(D), halt."

# Use swipl to execute the input string with the -q flag for quiet mode
swipl_output = subprocess.check_output(["swipl", "-q", "-t", input_string]).decode('utf-8').strip()
print(swipl_output)

# Use yap to execute the input string with the -q flag for quiet mode
yap_output = subprocess.check_output(["yap", "-q", "-t", input_string]).decode('utf-8').strip()
print(yap_output)