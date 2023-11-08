```python
class Test:
    def calc(self, func, value):
        result = func(value)
        print(result)

def main():
    test = Test()
    func_list = [func1, func2, func3]  # list of functions
    value = 10
    for func in func_list:
        test.calc(func, value)

def func1(value):
    return value * 2

def func2(value):
    return value + 5

def func3(value):
    return value ** 2

if __name__ == "__main__":
    main()
```