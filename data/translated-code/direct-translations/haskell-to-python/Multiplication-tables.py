from typing import List, Optional
import Data.Maybe

def mulTable(xs: List[int]) -> List[List[Optional[int]]]:
    labels = list(map(lambda x: Just(x), xs))
    table = [[upperMul(x, y) for y in xs] for x in xs]
    return [labels] + list(map(lambda x, y: [x] + y, labels, table))

def upperMul(x: int, y: int) -> Optional[int]:
    if x > y:
        return Nothing
    else:
        return Just(x * y)

def main() -> None:
    tables = [ [13, 14, 15, 16, 17, 18, 19, 20],
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
               [95, 96, 97, 98, 99, 100]
             ]
    for table in tables:
        print(showTable(mulTable(table)))

def showTable(xs: List[List[Optional[int]]]) -> str:
    w = len(str(fromMaybe(0, xs[-1][-1]))) + 1
    gap = ' ' * w
    rows = [list(map(lambda x: str(x).rjust(w, ' ') if x else gap, row)) for row in xs]
    return '\n'.join([' '.join(row) for row in rows])

if __name__ == "__main__":
    main()