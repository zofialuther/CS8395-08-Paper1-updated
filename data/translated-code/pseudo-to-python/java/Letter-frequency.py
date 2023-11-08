try:
    file_input = open("filename.txt", "r")
    data = file_input.read()
    hashmap = {}
    for char in data:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1
    file_input.close()
except IOError:
    print("Error handling the file")

# Use the hashmap to access and manipulate the data as needed
print(hashmap)