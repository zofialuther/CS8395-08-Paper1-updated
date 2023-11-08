```python
from array import array
import numpy as np

delimiters = ",;:"

def fields(xs):
    if not xs:
        return []
    else:
        item, rest = xs.split(delimiters[0], 1)
        next = rest.lstrip(delimiters)
        return [item] + fields(next)

def unfields(a):
    if a is None:
        return []
    else:
        ((_, _), (_, fieldNumber)) = a.bounds
        elems = a.flatten()
        result = []
        for i in range(0, len(elems), fieldNumber):
            result.append(','.join(elems[i:i+fieldNumber]))
        return result

def fieldArray(xs):
    if not xs:
        return None
    else:
        flat_list = [item for sublist in xs for item in sublist]
        shape = (len(xs), len(xs[0]))
        return np.array(flat_list).reshape(shape)

def fieldsFromFile(filepath):
    with open(filepath, 'r') as file:
        data = file.readlines()
        return fieldArray([fields(line) for line in data])

def fieldsToFile(filepath, a):
    with open(filepath, 'w') as file:
        file.write('\n'.join(unfields(a)))

def someChanges(a):
    if a is not None:
        a[(0,0)] = "changed"
        a[(2,3)] = "altered"
        a[(4,1)] = "modified"
    return a

def main():
    a = fieldsFromFile("example.txt")
    if a is not None:
        fieldsToFile("output.txt", someChanges(a))

main()
```