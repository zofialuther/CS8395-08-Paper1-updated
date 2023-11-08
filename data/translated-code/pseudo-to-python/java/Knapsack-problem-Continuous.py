class Item:
    def __init__(self):
        self.name = ""
        self.weight = 0
        self.value = 0
        self.inKnapsack = 0

    def __init__(self, item):
        self.setName(item.name)
        self.setWeight(item.weight)
        self.setValue(item.value)

    def __init__(self, _weight, _value):
        self.setWeight(_weight)
        self.setValue(_value)

    def __init__(self, _name, _weight, _value):
        self.setName(_name)
        self.setWeight(_weight)
        self.setValue(_value)

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

    def compareTo(self, item):
        result = 0
        i2 = item
        rate1 = self.value / self.weight
        rate2 = i2.value / i2.weight
        if (rate1 > rate2):
            result = -1
        elif (rate1 < rate2):
            result = 1
        return result