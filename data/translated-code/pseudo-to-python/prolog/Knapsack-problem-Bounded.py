from pyswip import Prolog, Functor, Variable, Query

prolog = Prolog()
prolog.consult("clpfd")

def knapsack():
    items = [("item1", 50, 60, 3), ("item2", 10, 100, 1), ("item3", 20, 120, 2)]
    weights, values, nb_items = zip(*items)
    scalar_product(weights, NbItems, #=<, 400),
    scalar_product(values, NbItems, #=, VM),
    time(labeling([max(VM)])),
    scalar_product(weights, NbItems, #=, WM),
    compute_lenword(items, MaxLen),
    print_results(items, NbItems, MaxLen).

def collect(items):
    for item in items:
        weight, value, nb_items = item
        yield (weight, value, nb_items)

def compute_lenword(items, MaxLen):
    MaxLen = max(len(name) for name, _, _, in items)

def print_results(items, NbItems, MaxLen):
    total_weight = sum(weight * nb for (weight, _, _), nb in zip(items, NbItems))
    total_value = sum(value * nb for (_, value, _), nb in zip(items, NbItems))
    print(f"Total weight: {total_weight}, Total value: {total_value}")
    for (name, weight, value), nb in zip(items, NbItems):
        if nb == 0:
            continue
        print(f"{name.ljust(MaxLen)} | Weight: {weight} | Value: {value}")

knapsack()