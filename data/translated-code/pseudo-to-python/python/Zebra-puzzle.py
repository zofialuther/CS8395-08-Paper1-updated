from constraint import Problem

problem = Problem()

problem.addVariables(["Nation", "Color", "Smoke", "Pet", "Drink"], [1, 2, 3, 4, 5])

problem.addConstraint(lambda Nation, Color, Smoke, Pet, Drink: len(set([Nation, Color, Smoke, Pet, Drink])) == 5)
# add actual constraints for the problem here

solution = problem.getSolution()

print("Nation:", solution["Nation"])
print("Color:", solution["Color"])
print("Smoke:", solution["Smoke"])
print("Pet:", solution["Pet"])
print("Drink:", solution["Drink"])