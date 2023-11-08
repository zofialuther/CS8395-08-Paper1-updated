```python
def show_args(default_param=10, *pos_args, **kw_args):
    print("Default parameter:", default_param)
    print("Positional arguments:", pos_args)
    print("Keyword arguments:", kw_args)

# Example calls
show_args()
show_args(20)
show_args(30, 40, 50)
show_args(60, 70, 80, key1='value1', key2='value2')

# Syntax error: positional arguments after keyword arguments
# show_args(key1='value1', key2='value2', 90, 100)
```