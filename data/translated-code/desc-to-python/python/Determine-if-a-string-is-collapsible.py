```python
def collapser(s):
    collapsed = ''
    for char in s:
        if len(collapsed) == 0 or char != collapsed[-1]:
            collapsed += char
    return collapsed

strings = ['hello', 'mississippi', 'aaaaabbbbbbccccdddddd']
for s in strings:
    collapsed_s = collapser(s)
    print(f'Original: {s}, Collapsed: {collapsed_s}, Original Size: {len(s)}, Collapsed Size: {len(collapsed_s)}')
```