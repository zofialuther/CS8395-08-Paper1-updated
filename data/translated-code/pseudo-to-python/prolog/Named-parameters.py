def sum(a, b, output):
    output = a + b

def named_args(args, kwargs):
    if not args:
        pass
    else:
        if args[0] in kwargs:
            named_args(args[1:], kwargs)
            
def main():
    output = 0
    sum(1, 2, output)
    print(output)

main()