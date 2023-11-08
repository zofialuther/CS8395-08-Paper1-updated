```python
def common_prefix(list1, list2):
    # function to find common prefix of two lists
    pass

def common_prefix_multiple(*lists):
    # function to find common prefix of zero or more lists
    pass

def split_path(path):
    # function to split a string into path components
    pass

def common_path(*paths):
    # function to find common prefix of zero or more paths
    pass

def main(paths):
    # main function
    common_dir = common_path(*[split_path(path) for path in paths])
    print(common_dir)

paths = ["/home/user/documents", "/home/user/downloads", "/home/user/music"]
main(paths)
```