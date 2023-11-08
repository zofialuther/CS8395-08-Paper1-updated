if __name__ == "__main__":
    main()

def main():
    sum(a=1, b=2, output=Output)
    print(Output)

def sum(**kwargs):
    named_args(kwargs, [a, b, output])
    output = kwargs['a'] + kwargs['b']

def named_args(args, kwargs):
    for arg in args:
        if arg not in kwargs:
            return False
    return True