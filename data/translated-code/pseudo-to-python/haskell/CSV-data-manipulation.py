def delimiters():
    return ",;:"

def fields(xs):
    if not xs:
        return []
    else:
        item, rest = xs.split(delimiters())
        _, next = rest.split(not_delimiters)
        return [item] + fields(next)

def unfields(a):
    if not a:
        return []
    else:
        fieldNumber = len(a)
        return [a[i] for i in range(0, len(a), fieldNumber)]

def fieldArray(xs):
    if not xs:
        return None
    else:
        return listArray(bounds, xs)

def fieldsFromFile(FilePath):
    with open(FilePath, 'r') as file:
        return fieldArray(map(fields, file.readlines()))

def fieldsToFile(FilePath, a):
    with open(FilePath, 'w') as file:
        file.write('\n'.join(unfields(a)))

def someChanges(a):
    return list(map(lambda x: x*2, a))

def main():
    a = fieldsFromFile("example.txt")
    if a:
        fieldsToFile("output.txt", someChanges(a))