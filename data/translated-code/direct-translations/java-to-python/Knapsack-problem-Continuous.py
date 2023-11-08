```python
class Item:

    def __init__(self, _name="", _weight=0, _value=0):
        self.name = _name
        self.weight = max(_weight, 0)
        self.value = max(_value, 0)
        self.inKnapsack = 0

    def setName(self, _name):
        self.name = _name

    def setWeight(self, _weight):
        self.weight = max(_weight, 0)

    def setValue(self, _value):
        self.value = max(_value, 0)

    def setInKnapsack(self, _inKnapsack):
        self.inKnapsack = max(_inKnapsack, 0)

    def checkMembers(self):
        self.setWeight(self.weight)
        self.setValue(self.value)
        self.setInKnapsack(self.inKnapsack)

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getValue(self):
        return self.value

    def getInKnapsack(self):
        return self.inKnapsack

    def __lt__(self, other):
        rate1 = self.value / self.weight
        rate2 = other.value / other.weight
        return rate1 < rate2

    def __gt__(self, other):
        rate1 = self.value / self.weight
        rate2 = other.value / other.weight
        return rate1 > rate2

    def __eq__(self, other):
        rate1 = self.value / self.weight
        rate2 = other.value / other.weight
        return rate1 == rate2
```