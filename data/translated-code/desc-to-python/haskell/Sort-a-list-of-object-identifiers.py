def splitString(string, character):
    return string.split(character)

def convertListToString(lst):
    return '.'.join(str(num) for num in lst)

def convertOIDtoList(oid):
    return [int(num) for num in oid.split('.')]

def orderOID(oids):
    return sorted(oids, key=convertOIDtoList)

def main():
    predefined_OIDs = ["1.3.6.1.2.1.1", "1.3.6.1.2.1.2", "1.3.6.1.2.1.3"]
    ordered_OIDs = orderOID(predefined_OIDs)
    print(ordered_OIDs)

main()