class ZeroOneKnapsack:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []
        self.calculated = False
        self.profit = 0
        self.solution_weight = 0

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def set_max_weight(self, max_weight):
        self.max_weight = max_weight

    def calculate_solution(self):
        # Dynamic programming method to calculate solution
        # ...
        self.calculated = True

    def get_solution_profit(self):
        return self.profit

    def get_solution_weight(self):
        return self.solution_weight

    def is_solution_calculated(self):
        return self.calculated