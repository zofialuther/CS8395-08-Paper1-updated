def hashJoin(records1, idx1, records2, idx2):
    result = []
    map = {}

    for record in records1:
        v = map.get(record[idx1], [])
        v.append(record)
        map[record[idx1]] = v

    for record in records2:
        lst = map.get(record[idx2])
        if lst is not None:
            for r in lst:
                result.append([r, record])

    return result

table1 = [["27", "Jonah"], ["18", "Alan"], ["28", "Glory"], ["18", "Popeye"], ["28", "Alan"]]
table2 = [["Jonah", "Whales"], ["Jonah", "Spiders"], ["Alan", "Ghosts"], ["Alan", "Zombies"], ["Glory", "Buffy"], ["Bob", "foo"]]

for r in hashJoin(table1, 1, table2, 0):
    print(r)