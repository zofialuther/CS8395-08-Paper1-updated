def func1(f):
    return f("a string")

def func2(s):
    return "func2 called with " + s

result = func1(func2)
print(result)