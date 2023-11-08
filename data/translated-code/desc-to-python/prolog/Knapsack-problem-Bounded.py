```python
from constraint import Problem, AllDifferentConstraint, MinSumConstraint

def knapsack(items, weight_limit):
    problem = Problem()
    
    for i, (name, weight, value, num_pieces) in enumerate(items):
        problem.addVariable(f'x{i}', range(num_pieces + 1))
    
    problem.addConstraint(MinSumConstraint(weight), [f'x{i}' for i in range(len(items))])
    problem.addConstraint(MinSumConstraint(0), [f'x{i}' for i in range(len(items))])
    
    def total_value(*selection):
        return sum(selection[i] * items[i][2] for i in range(len(items)))
    
    problem.addConstraint(lambda *selection: total_value(*selection) <= value, [f'x{i}' for i in range(len(items))])
    
    solutions = problem.getSolutions()
    max_value = max(total_value(*[sol[f'x{i}'] for i in range(len(items))]) for sol in solutions)
    selected_items = [items[i] for i in range(len(items)) if solutions[0][f'x{i}'] > 0]
    
    return max_value, selected_items

def item_name_length(items):
    return max(len(item[0]) for item in items)

def print_results(max_value, selected_items):
    name_length = item_name_length(selected_items)
    print(f"{'Item':<{name_length}} {'Weight':<7} {'Value':<7}")
    print('-' * (name_length + 16))
    for item in selected_items:
        print(f"{item[0]:<{name_length}} {item[1]:<7} {item[2]:<7}")
    print(f"\nTotal value: {max_value}")

items = [('item1', 2, 3, 2), ('item2', 3, 4, 1), ('item3', 5, 8, 3)]
weight_limit = 5

max_value, selected_items = knapsack(items, weight_limit)
print_results(max_value, selected_items)
```