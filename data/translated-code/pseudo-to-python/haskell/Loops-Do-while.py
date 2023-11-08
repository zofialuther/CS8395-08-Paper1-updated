```python
def main():
    lst = [0]
    
    def condition():
        return lst[0] > 0 and lst[0] % 6 == 0
    
    def function():
        lst[0] += 1
    
    while not condition():
        function()
    
    reversed_lst = list(reversed(lst))
    
    for elem in reversed_lst:
        print(elem)

main()
```