from itertools import product

def main():
    for x, y, z in product("abc", "ABC", "123"):
        print(x, y, z)

main()