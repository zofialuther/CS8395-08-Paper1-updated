class Item:
    def __init__(self, name, weight, value, knapsack_weight):
        self.name = name
        self.weight = weight
        self.value = value
        self.knapsack_weight = knapsack_weight

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_knapsack_weight(self, knapsack_weight):
        self.knapsack_weight = knapsack_weight

    def get_knapsack_weight(self):
        return self.knapsack_weight

    def __lt__(self, other):
        return self.value / self.weight < other.value / other.weight