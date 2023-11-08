```python
def stripcomment(A, B):
    comment_index = min(A.find(';'), A.find('#'))
    if comment_index != -1:
        B = A[:comment_index]
    else:
        B = A
    return B

def start(input_string):
    modified_string = ""
    print(stripcomment(input_string, modified_string))
```