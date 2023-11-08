You can use the following Python code:

from math import pow

power = pow(5, pow(4, pow(3, 2)))
str = str(power)
len = len(str)
print(f"5**4**3**2 = {str[:20]}...{str[-20:]} and has {len} digits")