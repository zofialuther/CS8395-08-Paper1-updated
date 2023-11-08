collection = [0, '1']
x = collection[0]
collection.append(2)
collection.insert(0, '-1')
y = collection[0]
collection.extend([2,'3'])
collection += [2,'3']
collection[2:6]
len(collection)
collection = (0, 1)
collection[:]
collection[-4:-1]
collection[::2]
collection="some string"
x = collection[::-1]
collection[::2] == "some string"[::2]
collection.__getitem__(slice(0,len(collection),2))
collection = {0: "zero", 1: "one"}
collection['zero'] = 2
collection = set([0, '1'])