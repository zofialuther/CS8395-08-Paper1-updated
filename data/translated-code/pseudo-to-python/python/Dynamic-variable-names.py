name = input("Enter a variable name: ")
globals()[name] = 42
print(globals()[name])