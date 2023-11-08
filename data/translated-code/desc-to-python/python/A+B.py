try:
    input_function = raw_input
except NameError:
    input_function = input

user_input = input_function("Enter numbers separated by spaces: ")
numbers = user_input.split()
numbers = [int(num) for num in numbers]
sum_of_numbers = sum(numbers)

print("The sum of the numbers is:", sum_of_numbers)