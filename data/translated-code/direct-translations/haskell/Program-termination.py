```python
import sys

def exit_with_success():
    sys.exit(0)

def exit_with_failure(error_code):
    sys.exit(error_code)

def exit_success():
    sys.exit(0)

def exit_failure():
    sys.exit(1)

# usage
problem = True

if problem:
    exit_with_success()                    # success
    exit_with_failure(2)                   # some failure with code
    exit_success()                         # success
    exit_failure()                         # generic failure
```