from collections import defaultdict

def hash_join(table1, index1, table2, index2):
    hash_table = defaultdict(list)
    for row in table1:
        hash_table[row[index1]].append(row)
    
    result = []
    for row in table2:
        for match in hash_table[row[index2]]:
            result.append((match, row))
    
    return result

# Example tables
table1 = [
    (1, 'Alice'),
    (2, 'Bob'),
    (3, 'Charlie')
]

table2 = [
    (1, 'Engineer'),
    (2, 'Doctor'),
    (3, 'Chef')
]

# Perform hash join
result = hash_join(table1, 0, table2, 0)

# Print results
for row in result:
    print(row)