```python
def main():
    Oid_list = ["1.3.6.1.4.1.11.2.17.19.3.4.0.10", 
                "1.3.6.1.4.1.11.2.17.5.2.0.79", 
                "1.3.6.1.4.1.11.2.17.19.3.4.0.4", 
                "1.3.6.1.4.1.11150.3.4.0.1", 
                "1.3.6.1.4.1.11.2.17.19.3.4.0.1", 
                "1.3.6.1.4.1.11150.3.4.0"]
    Sorted_list = sort_oid_list(Oid_list)
    for Oid in Sorted_list:
        print(Oid)

def sort_oid_list(Oid_list):
    Parsed = parse_oid_list(Oid_list)
    Sorted = sorted(Parsed)
    return Sorted

def parse_oid_list(Oid_list):
    Parsed = []
    for Oid in Oid_list:
        Numbers = parse_oid(Oid)
        Parsed.append(oid(Numbers, Oid))
    return Parsed

def parse_oid(Oid):
    Strings = Oid.split(".")
    Numbers = number_strings(Strings)
    return Numbers

def number_strings(Strings):
    Numbers = []
    for String in Strings:
        Number = int(String)
        Numbers.append(Number)
    return Numbers
```