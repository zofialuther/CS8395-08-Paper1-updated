user_input = input("Enter a sentence: ")
words = user_input.split()
numbers = [len(word) for word in words]
total_sum = sum(numbers)
print(total_sum)