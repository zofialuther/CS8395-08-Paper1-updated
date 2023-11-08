```python
import System.IO

def hInteract(func, input_handle, output_handle):
    output_handle.write(func(input_handle.read()))

def processByTemp(func, file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    with open(file_name, 'w') as file:
        file.write(func(data))

def process(func, file_names):
    if not file_names:
        hInteract(func, System.IO.StdIn, System.IO.StdOut)
    else:
        for file_name in file_names:
            with open(file_name, 'r') as file:
                data = file.read()
            with open(file_name, 'w') as file:
                file.write(func(data))
```