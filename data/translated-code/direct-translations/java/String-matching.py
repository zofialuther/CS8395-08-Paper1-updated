s = "hello"
suffix = "lo"

if s[len(s) - len(suffix):] == suffix:
    print(True)
else:
    print(False)