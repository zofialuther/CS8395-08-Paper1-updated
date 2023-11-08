```python
# Python code
def hashJoin(table1, table2, index):
    result = []
    hash_map = {}

    for record in table1:
        key = record[index]
        if key not in hash_map:
            hash_map[key] = [record]
        else:
            hash_map[key].append(record)

    for record in table2:
        key = record[index]
        if key in hash_map:
            for match in hash_map[key]:
                result.append(match + record)

    print(result)

table1 = [ [1, 'a'], [2, 'b'], [3, 'c'] ]
table2 = [ [2, 'x'], [3, 'y'], [4, 'z'] ]

hashJoin(table1, table2, 0)
```