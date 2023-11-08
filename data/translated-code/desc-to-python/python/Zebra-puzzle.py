from constraint import *

problem = Problem()

nationality = ['English', 'Spanish', 'Ukrainian', 'Norwegian', 'Japanese']
color = ['Red', 'Green', 'Ivory', 'Yellow', 'Blue']
cigarette = ['Kools', 'Chesterfields', 'Old Gold', 'Lucky Strike', 'Parliaments']
pet = ['Dog', 'Snails', 'Fox', 'Horse', 'Zebra']
drink = ['Coffee', 'Tea', 'Milk', 'Orange Juice', 'Water']

problem.addVariables(nationality, range(1, 6))
problem.addVariables(color, range(1, 6))
problem.addVariables(cigarette, range(1, 6))
problem.addVariables(pet, range(1, 6))
problem.addVariables(drink, range(1, 6))

problem.addConstraint(AllDifferentConstraint(), nationality)
problem.addConstraint(AllDifferentConstraint(), color)
problem.addConstraint(AllDifferentConstraint(), cigarette)
problem.addConstraint(AllDifferentConstraint(), pet)
problem.addConstraint(AllDifferentConstraint(), drink)

# Add other constraints based on given clues

solutions = problem.getSolutions()

for solution in solutions:
    print(solution)