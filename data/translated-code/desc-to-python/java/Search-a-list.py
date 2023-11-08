from java.util import Arrays

haystack = ["New York", "California", "Washington", "Texas", "Florida", "Georgia", "Bush"]

index_washington = Arrays.binarySearch(haystack, "Washington")
index_bush = Arrays.binarySearch(haystack, "Bush")

if index_washington < 0:
    print("Washington is not in the haystack")
else:
    print("Index of Washington in the haystack:", index_washington)
    print("Washington:", haystack[index_washington])

if index_bush < 0:
    print("Bush is not in the haystack")
else:
    print("Index of Bush in the haystack:", index_bush)
    print("Bush:", haystack[index_bush])