```python
def sum(**kwargs):
    if 'value1' in kwargs and 'value2' in kwargs:
        return kwargs['value1'] + kwargs['value2']

def main():
    named_args = {'value1': 5, 'value2': 10}
    result = sum(**named_args)
    print(result)

main()
```