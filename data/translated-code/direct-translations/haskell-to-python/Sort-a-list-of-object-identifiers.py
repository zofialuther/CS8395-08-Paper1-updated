from dataclasses import dataclass
from typing import List

def splitString(c, s):
    if not s:
        return []
    else:
        item, rest = s.split(c, 1)
        _, next = rest.split(c, 1)
        return [item] + splitString(c, next)

def convertIntListToString(int_list):
    return ".".join(map(str, int_list))

def orderOID(oid_list):
    return list(map(convertIntListToString, sorted(map(lambda x: list(map(int, splitString('.', x))), oid_list)))

oid = [
    "1.3.6.1.4.1.11.2.17.19.3.4.0.10",
    "1.3.6.1.4.1.11.2.17.5.2.0.79",
    "1.3.6.1.4.1.11.2.17.19.3.4.0.4",
    "1.3.6.1.4.1.11150.3.4.0.1",
    "1.3.6.1.4.1.11.2.17.19.3.4.0.1",
    "1.3.6.1.4.1.11150.3.4.0"
]

def main():
    for result in orderOID(oid):
        print(result)

main()