```python
# 1. Define type Result as a list of tuples where the first element is a String and the second element is a list of Integers.
Result = list[tuple[str, list[int]]]

# 2. Define function oneMillionPrimes to generate a list of primes less than 1,000,000.
def oneMillionPrimes():
    # function implementation

# 3. Define function getGroups that takes a list of Integers and returns a Result.
def getGroups(nums: list[int]) -> Result:
    if len(nums) == 0:
        return []
    elif len(nums) >= 4:
        # check differences and add tuples to Result
    else:
        return getGroups(nums[1:])

# 4. Define a global variable groups that stores the Result obtained by calling getGroups with oneMillionPrimes.
groups = getGroups(oneMillionPrimes())

# 5. Define function showGroup that takes a String and prints information about the groups that match the given String.
def showGroup(s: str):
    # print number of groups that match the String and first and last elements of each matching group

# 6. Define the main function to call showGroup with specific Strings in a sequence.
def main():
    showGroup("example1")
    showGroup("example2")
    showGroup("example3")

if __name__ == "__main__":
    main()
```