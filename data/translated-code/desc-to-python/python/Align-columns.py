```python
def aligner(input_file, justification_type):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    max_widths = [0] * len(lines[0].split('$'))
    
    for line in lines:
        fields = line.split('$')
        for i in range(len(fields)):
            max_widths[i] = max(max_widths[i], len(fields[i]))
    
    output = ''
    for line in lines:
        fields = line.split('$')
        for i in range(len(fields)):
            if justification_type == 'Left':
                output += fields[i].ljust(max_widths[i] + 1)
            elif justification_type == 'Right':
                output += fields[i].rjust(max_widths[i] + 1)
            elif justification_type == 'Center':
                output += fields[i].center(max_widths[i] + 2)
        output += '\n'
    
    return output

input_file = 'filename.txt'

print("Left Justified:")
print(aligner(input_file, 'Left'))

print("Right Justified:")
print(aligner(input_file, 'Right'))

print("Center Justified:")
print(aligner(input_file, 'Center'))
```