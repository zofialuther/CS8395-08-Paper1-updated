```python
def find_common_path(*paths):
    common_path = ""
    
    for i in range(len(paths[0])):
        folder = paths[0][i]
        for path in paths:
            if i >= len(path) or path[i] != folder:
                return common_path
        common_path += folder + "/"
    
    return common_path
```