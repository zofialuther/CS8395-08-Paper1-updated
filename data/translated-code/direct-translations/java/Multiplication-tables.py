```python
class MultiplicationTable:
    def main(self):
        for i in range(1, 13):
            print("\t" + str(i), end="")
        
        print()
        for i in range(100):
            print("-", end="")
        print()
        for i in range(1, 13):
            print(str(i) + "|", end="")
            for j in range(1, 13):
                print("\t", end="")
                if j >= i:
                    print("\t" + str(i * j), end="")
            print()

multiplication_table = MultiplicationTable()
multiplication_table.main()
```