y = str(5**4**3**2)
first_part = y[:20]
last_part = y[-20:]
number_of_digits = len(y)
print("5**4**3**2 = %s...%s and has %i digits" % (first_part, last_part, number_of_digits))