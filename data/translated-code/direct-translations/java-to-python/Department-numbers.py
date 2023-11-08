```python
class DepartmentNumbers:
    @staticmethod
    def main(args):
        print("Police  Sanitation  Fire")
        print("------  ----------  ----")
        count = 0
        for i in range(2, 7, 2):
            for j in range(1, 8):
                if j == i:
                    continue
                for k in range(1, 8):
                    if k == i or k == j:
                        continue
                    if i + j + k != 12:
                        continue
                    print("  {}         {}         {}".format(i, j, k))
                    count += 1
        print("\n{} valid combinations".format(count))


DepartmentNumbers.main([])
```