```python
def parse_oid(oid):
    return tuple(map(int, oid.split('.')))

def sort_oid_list(oid_list):
    parsed_oids = [parse_oid(oid) for oid in oid_list]
    sorted_oids = sorted(parsed_oids)
    return ['.'.join(map(str, oid)) for oid in sorted_oids]

input_list = ["1.3.6.1.2.1", "1.3.6.1.2.1.1", "1.3.6.1.2.1.11", "1.3.6.1.2.10", "1.3.6.1.2.2"]
sorted_list = sort_oid_list(input_list)
print(sorted_list)
```