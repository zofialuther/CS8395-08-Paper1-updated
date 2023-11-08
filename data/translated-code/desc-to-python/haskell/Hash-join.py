def hashJoin(list1, list2, keyFunc1, keyFunc2):
    hash_table = {}
    result = []
    
    for item in list1:
        key = keyFunc1(item)
        if key in hash_table:
            hash_table[key].append(item)
        else:
            hash_table[key] = [item]
    
    for item in list2:
        key = keyFunc2(item)
        if key in hash_table:
            for i in hash_table[key]:
                result.append((i, item))
    
    return result

# Example usage
def key1(x):
    return x % 2

def key2(x):
    return x % 2

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]

result = hashJoin(list1, list2, key1, key2)
print(result)