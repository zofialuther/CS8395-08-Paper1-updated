```python
def ordSuff(num):
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    return str(num) + suffix

ordSuffs = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']

def printOrdSuffs(nums):
    for num in nums:
        print(ordSuff(num))

def main():
    printOrdSuffs(range(1, 11))
    printOrdSuffs(range(101, 111))

main()
```