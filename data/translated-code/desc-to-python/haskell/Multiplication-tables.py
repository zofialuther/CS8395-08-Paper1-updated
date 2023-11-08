```python
from typing import List, Union

class Maybe:
    def __init__(self, value: Union[int, None]):
        self.value = value

def mulTable(nums: List[int]) -> List[List[Maybe]]:
    table = [[Maybe(None) for _ in range(len(nums))] for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            table[i][j] = Maybe(nums[i] * nums[j])
    return table

def showTable(table: List[List[Maybe]]) -> None:
    for row in table:
        for cell in row:
            if cell.value is not None:
                print(str(cell.value).rjust(5), end='')
            else:
                print("  -  ", end='')
        print()

def main():
    nums = range(1, 6)
    table = mulTable(nums)
    showTable(table)

if __name__ == "__main__":
    main()
```