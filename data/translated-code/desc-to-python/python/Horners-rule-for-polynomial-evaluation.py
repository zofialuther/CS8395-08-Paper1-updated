import numpy as np

coefficients = (-19, 7, -4, 6)
value = 3

result = np.polyval(coefficients, value)
print(result)