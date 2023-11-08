```python
class ZeroOneKnapsack:
    def __init__(self, max_weight, item_list):
        self.max_weight = max_weight
        self.item_list = item_list
        self.num_items = len(item_list)
        self.profit = 0
        self.solution_weight = 0
        self.solution = [[0 for _ in range(max_weight + 1)] for _ in range(self.num_items + 1)]

    def calculate_solution(self):
        for i in range(1, self.num_items + 1):
            for w in range(self.max_weight + 1):
                if self.item_list[i - 1][1] <= w:
                    self.solution[i][w] = max(self.item_list[i - 1][0] + self.solution[i - 1][w - self.item_list[i - 1][1]], self.solution[i - 1][w])
                else:
                    self.solution[i][w] = self.solution[i - 1][w]
        self.profit = self.solution[self.num_items][self.max_weight]
        self.solution_weight = self.max_weight
        w = self.max_weight
        items = []
        for i in range(self.num_items, 0, -1):
            if self.profit <= 0:
                break
            if self.profit == self.solution[i - 1][w]:
                continue
            else:
                items.append(self.item_list[i - 1])
                self.profit -= self.item_list[i - 1][0]
                w -= self.item_list[i - 1][1]
        self.solution_weight -= w
        return items

    def add_item(self, item):
        self.item_list.append(item)
        self.num_items += 1

    def remove_item(self, index):
        del self.item_list[index]
        self.num_items -= 1

    def get_profit(self):
        return self.profit

    def get_solution_weight(self):
        return self.solution_weight

    def set_max_weight(self, weight):
        self.max_weight = weight

    def set_item_list(self, items):
        self.item_list = items

    def initialize_state(self):
        self.solution = [[0 for _ in range(self.max_weight + 1)] for _ in range(self.num_items + 1)]
```