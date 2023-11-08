# This code calculates the average of a list of numbers
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers) if len(numbers) > 0 else 0.0