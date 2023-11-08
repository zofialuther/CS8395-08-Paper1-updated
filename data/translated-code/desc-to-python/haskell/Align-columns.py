```python
def align_text(file, justification):
    with open(file, 'r') as f:
        lines = f.readlines()
    
    words = [line.strip().split('$') for line in lines]
    columns = zip(*words)
    max_lengths = [max(len(word) for word in column) for column in columns]
    
    aligned_text = ''
    for line in words:
        for i, word in enumerate(line):
            aligned_text += word.ljust(max_lengths[i]) if justification == 'left' else word.rjust(max_lengths[i]) if justification == 'right' else word.center(max_lengths[i])
            if i < len(line) - 1:
                aligned_text += ' '
        aligned_text += '\n'
    
    return aligned_text
```