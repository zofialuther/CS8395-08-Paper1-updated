```python
import itertools

def solve24(nums):
    ops = ['+', '-', '*', '/']
    def helper(nums):
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if i != j:
                    for op in ops:
                        if (op == '+' or op == '*') and i > j:
                            continue
                        if op == '/' and b == 0:
                            continue
                        newNums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        if op == '+':
                            newNums.append(a + b)
                        elif op == '-':
                            newNums.append(a - b)
                        elif op == '*':
                            newNums.append(a * b)
                        elif op == '/':
                            newNums.append(a / b)
                        if helper(newNums):
                            return True
                        newNums.pop()
        return False
    
    return helper(nums)

# Test cases
print(solve24([4, 1, 8, 7]))  # True
print(solve24([8, 3, 6, 6]))  # True
print(solve24([1, 1, 1, 1]))  # False
```