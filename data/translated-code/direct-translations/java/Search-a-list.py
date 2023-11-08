haystack = ["Zig","Zag","Wally","Ronald","Bush","Krusty","Charlie","Bush","Bozo"]

for needle in ["Washington","Bush"]:
    index = haystack.index(needle) if needle in haystack else -1
    if index < 0:
        print(needle + " is not in haystack")
    else:
        print(str(index) + " " + needle)