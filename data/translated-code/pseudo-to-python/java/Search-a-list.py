import java.util.Arrays

haystack = ["Zig","Zag","Wally","Ronald","Bush","Krusty","Charlie","Bush","Bozo"]

for needle in ["Washington","Bush"]:
    index = Arrays.binarySearch(haystack, needle)
    if index < 0:
        print("needle is not in haystack")
    else:
        print(index, needle)