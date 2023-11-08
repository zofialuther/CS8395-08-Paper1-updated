s = ""

# method 1
if len(s) == 0:
    print("String is empty")

# method 2
if not s:
    print("String is empty")

# method 3
if s == "":
    print("String is empty")

def emptystring(s):
    if s is None or not s:
        return True
    else:
        return False