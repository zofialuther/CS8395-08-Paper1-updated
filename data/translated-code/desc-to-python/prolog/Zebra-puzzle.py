from itertools import permutations
import clpfd

# Define the variables for the five categories
nationality = clpfd.FiniteDomain(1, 5)
house_color = clpfd.FiniteDomain(1, 5)
cigarette_brand = clpfd.FiniteDomain(1, 5)
pet = clpfd.FiniteDomain(1, 5)
favorite_drink = clpfd.FiniteDomain(1, 5)

# Define the constraints for the variables
constraints = [
    nationality != house_color,
    nationality != cigarette_brand,
    nationality != pet,
    nationality != favorite_drink,
    house_color != cigarette_brand,
    house_color != pet,
    house_color != favorite_drink,
    cigarette_brand != pet,
    cigarette_brand != favorite_drink,
    pet != favorite_drink
]

# Use the CLPFD library to solve the puzzle
solution = clpfd.solve(constraints)

# Print the solution
print(solution)