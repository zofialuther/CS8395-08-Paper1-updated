import inspect

current_file_path = inspect.getfile(inspect.currentframe())
print(current_file_path)