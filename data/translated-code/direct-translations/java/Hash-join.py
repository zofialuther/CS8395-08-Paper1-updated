```python
def hash_join(records1, idx1, records2, idx2):
    result = []
    map = {}

    for record in records1:
        if record[idx1] in map:
            map[record[idx1]].append(record)
        else:
            map[record[idx1]] = [record]

    for record in records2:
        if record[idx2] in map:
            for r in map[record[idx2]]:
                result.append([r, record])
    
    return result

table1 = [["27", "Jonah"], ["18", "Alan"], ["28", "Glory"], ["18", "Popeye"], ["28", "Alan"]]
table2 = [["Jonah", "Whales"], ["Jonah", "Spiders"], ["Alan", "Ghosts"], ["Alan", "Zombies"], ["Glory", "Buffy"], ["Bob", "foo"]]

result = hash_join(table1, 1, table2, 0)
for r in result:
    print(r)
```