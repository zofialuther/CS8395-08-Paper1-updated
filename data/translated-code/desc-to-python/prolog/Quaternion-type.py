data_points = [1, 2, 3, 4, 5]

# Absolute value
abs_values = [abs(x) for x in data_points]
print(abs_values)

# Negating
negated_values = [-x for x in data_points]
print(negated_values)

# Conjugating
conjugated_values = [x.conjugate() for x in data_points]
print(conjugated_values)

# Adding
added_values = [x + 10 for x in data_points]
print(added_values)

# Multiplying
multiplied_values = [x * 2 for x in data_points]
print(multiplied_values)