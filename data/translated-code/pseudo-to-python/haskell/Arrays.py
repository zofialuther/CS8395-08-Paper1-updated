from Data.Array import IO

def main():
    arr = IO.array(1, 10, 37)
    a = arr[1]
    arr[1] = 64
    b = arr[1]
    print(a, b)