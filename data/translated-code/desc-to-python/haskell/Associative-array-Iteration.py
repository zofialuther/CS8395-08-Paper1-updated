import Data.Map as M

def main():
    myMap = M.fromList([("a", 1), ("b", 2), ("c", 3)])
    print("List of key-value pairs:", M.toList(myMap))
    print("Keys:", M.keys(myMap))
    print("Values:", M.elems(myMap))

main()