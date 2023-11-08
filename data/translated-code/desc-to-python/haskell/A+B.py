user_input = input("Enter a line of text: ")
words = user_input.split()
numbers = [len(word) for word in words]
sum_of_numbers = sum(numbers)
print("The sum of the numbers is:", sum_of_numbers)