def repeat(callable, times):
    if times <= 0:
        return
    callable()
    repeat(callable, times-1)

def test():
    print('Hello, World')

def test_with_name(name):
    print('Hello, ', name)