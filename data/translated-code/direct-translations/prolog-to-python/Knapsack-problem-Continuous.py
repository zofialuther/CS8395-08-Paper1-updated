from pysimplex import Variable, Model

def knapsack():
    L = [("beef", 3.8, 36),
         ("pork", 5.4, 43),
         ("ham", 3.6, 90),
         ("greaves", 2.4, 45),
         ("flitch", 4.0, 30),
         ("brawn", 2.5, 56),
         ("welt", 3.7, 67),
         ("salami", 3.0, 95),
         ("sausage", 5.9, 98)]

    model = Model()
    variables = []

    for i, (name, weight, value) in enumerate(L):
        x = Variable(f"x{i+1}", lb=0, ub=weight)
        variables.append(x)
        model += x * (value/weight)

    model += sum(variables) <= 15.0

    results = model.maximize()
    result_values = [var.value for var in variables]

    for i, (name, weight, value) in enumerate(L):
        print(f"{name}\t{result_values[i]}\t{result_values[i] * value / weight}")

knapsack()