```python
# Python does not have built-in parallel streams equivalent to Java
# but the functionality can be achieved using multiprocessing or threading
# The properDivsSum method will need to be implemented separately

def properDivsSum(num):
    # implementation of properDivsSum method

def findAmicableNumbers(limit):
    nums_sum_divs = {}
    for num in range(1, limit+1):
        nums_sum_divs[num] = properDivsSum(num)
    
    for num, divs_sum in nums_sum_divs.items():
        if divs_sum in nums_sum_divs and nums_sum_divs[divs_sum] == num and num != divs_sum:
            print(f"Amicable pair: {num} and {divs_sum}")

# Call the findAmicableNumbers method with the specified limit
findAmicableNumbers(1000)
```