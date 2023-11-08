myDict = { "hello": 13, "world": 31, "!" : 71 }

# iterating over key-value pairs:
for key, value in myDict.items():
    print("key =" + key + ", value =" + str(value))

# iterating over keys:
for key in myDict:
    print("key =" + key)

# iterating over values:
for value in myDict.values():
    print("value =" + str(value))