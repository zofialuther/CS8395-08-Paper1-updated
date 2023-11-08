```python
def pseudocode_for_classes():
    classes = (str.isupper, str.islower, str.isalnum, str.isalpha, str.isdecimal, str.isdigit, str.isidentifier, str.isnumeric, str.isprintable, str.isspace, str.istitle)
    for stringclass in classes:
        chars = ''
        for i in range(0x10FFFF+1):
            if stringclass(chr(i)) is True:
                chars = chars + chr(i)
        print('String class ' + stringclass.__name__ + ' has ' + str(len(chars)) + ' characters the first of which are:\n' + chars[:100])

pseudocode_for_classes()
```