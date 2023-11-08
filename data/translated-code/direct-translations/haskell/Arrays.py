import array as arr

def main():
    array = arr.array('i', [37]*10)
    a = array[0]
    array[0] = 64
    b = array[0]
    print(a, b)

main()