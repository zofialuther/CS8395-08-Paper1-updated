from typing import List, Optional

def mulTable(nums: List[int]) -> List[List[Optional[int]]]:
    def upperMul(x: int, y: int) -> Optional[int]:
        if x <= y:
            return x * y
        else:
            return None
    
    labels = [Maybe(x) for x in nums]
    table = [[Nothing] + labels]
    for num1 in nums:
        row = [Maybe(upperMul(num1, num2)) for num2 in nums]
        table.append(row)
    
    return table

def main() -> None:
    result1 = mulTable([1, 2, 3])
    result2 = mulTable([4, 5, 6])
    result3 = mulTable([7, 8, 9])
    print(showTable(result1))
    print(showTable(result2))
    print(showTable(result3))

def showTable(table: List[List[Optional[int]]]) -> str:
    cell_width = len(str(table[-1][-1]))
    gap = [' ' * cell_width]
    formatted_table = [['{0}'.format(str(x).rjust(cell_width, ' ')) for x in row] for row in table]
    return '\n'.join(['  '.join(row) for row in formatted_table])