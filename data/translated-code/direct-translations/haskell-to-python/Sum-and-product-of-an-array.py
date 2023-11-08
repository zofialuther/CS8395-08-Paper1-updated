from Data.Array import listArray, elems

def main():
    array = listArray(1, 10, [11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    functions = [sum, product]
    result = [func(elems(array)) for func in functions]
    for res in result:
        print(res)

main()