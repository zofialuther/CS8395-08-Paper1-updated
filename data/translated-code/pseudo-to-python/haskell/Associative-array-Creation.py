def lookup(key, dictionary):
    for pair in dictionary:
        if pair[0] == key:
            return pair[1]
    return None

dict = [("key1","val1"), ("key2","val2")]
ans = lookup("key2", dict)