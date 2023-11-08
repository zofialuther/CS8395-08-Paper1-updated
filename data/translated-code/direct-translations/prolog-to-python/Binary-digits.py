def binary(X):
    print(format(X, 'b'))

def main():
    numbers = [5, 50, 9000]
    list(map(binary, numbers))
    exit()

main()