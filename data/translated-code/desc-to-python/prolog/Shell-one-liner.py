```python
import subprocess

def check_prolog_dialect():
    result = subprocess.run(['echo', 'current_prolog_flag(version_data, SWI) ; current_prolog_flag(version_data, YAP).'], text=True, capture_output=True, shell=True)
    if "SWI" in result.stdout:
        print("swi")
    elif "YAP" in result.stdout:
        print("yap")
    else:
        print("Unknown Prolog dialect")

check_prolog_dialect()
```