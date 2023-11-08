def func1(func):
    return func("a string")

def func2(string):
    return "func2 called with " + string

def main():
    result = func1(func2)
    print(result)

main()