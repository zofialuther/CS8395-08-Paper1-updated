try:
    raw_input
except:
    raw_input = input

user_input = raw_input()
numbers = user_input.split()
numbers = list(map(int, numbers))
result = sum(numbers)
print(result)