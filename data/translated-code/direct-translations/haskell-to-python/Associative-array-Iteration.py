import Data.Map as M

myMap = M.fromList([("hello", 13), ("world", 31), ("!", 71)])

def main():
    print("\n".join([str(M.toList(myMap)), str(M.keys(myMap)), str(M.elems(myMap))]))