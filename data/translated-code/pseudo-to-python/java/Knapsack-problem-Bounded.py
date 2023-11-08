class ZeroOneKnapsack:
    def __init__(self):
        self.itemList = []
        self.maxWeight = 0
        self.solutionWeight = 0
        self.profit = 0
        self.calculated = False

    def __init__(self, _maxWeight):
        self.maxWeight = _maxWeight

    def __init__(self, _itemList):
        self.itemList = _itemList

    def __init__(self, _itemList, _maxWeight):
        self.itemList = _itemList
        self.maxWeight = _maxWeight

    def calcSolution(self):
        n = len(self.itemList)
        self.setInitialStateForCalculation()
        if n > 0 and self.maxWeight > 0:
            c = [[]]
            curr = []
            c.append(curr)
            for j in range(self.maxWeight):
                curr.append(0)
            for i in range(1, n+1):
                prev = curr
                c.append(curr)
                curr = []
                for j in range(self.maxWeight):
                    if j > 0:
                        wH = self.itemList[i-1].getWeight()
                        if wH > j:
                            curr.append(prev[j])
                        else:
                            curr.append(max(prev[j], self.itemList[i-1].getValue() + prev[j-wH]))
                    else:
                        curr.append(0)
            profit = curr[self.maxWeight]
            for i in range(n, 0, -1):
                for j in range(self.maxWeight, 0, -1):
                    tempI = c[i][j]
                    tempI_1 = c[i-1][j]
                    if (i == 0 and tempI > 0) or (i > 0 and tempI != tempI_1):
                        iH = self.itemList[i-1]
                        wH = iH.getWeight()
                        iH.setInKnapsack(1)
                        j -= wH
                        self.solutionWeight += wH
            self.calculated = True
        return self.itemList

    def add(self, name, weight, value):
        if name == "":
            name = str(len(self.itemList) + 1)
        self.itemList.append(Item(name, weight, value))
        self.setInitialStateForCalculation()

    def add(self, weight, value):
        self.add("", weight, value)

    def remove(self, name):
        self.itemList = [item for item in self.itemList if item.getName() != name]
        self.setInitialStateForCalculation()

    def removeAllItems(self):
        self.itemList.clear()
        self.setInitialStateForCalculation()

    def getProfit(self):
        if not self.calculated:
            self.calcSolution()
        return self.profit

    def getSolutionWeight(self):
        return self.solutionWeight

    def isCalculated(self):
        return self.calculated

    def getMaxWeight(self):
        return self.maxWeight

    def setMaxWeight(self, _maxWeight):
        self.maxWeight = max(_maxWeight, 0)

    def setItemList(self, _itemList):
        if _itemList is not None:
            self.itemList = _itemList
            for item in _itemList:
                item.checkMembers()

    def setInKnapsackByAll(self, inKnapsack):
        for item in self.itemList:
            if inKnapsack > 0:
                item.setInKnapsack(1)
            else:
                item.setInKnapsack(0)

    def setInitialStateForCalculation(self):
        self.setInKnapsackByAll(0)
        self.calculated = False
        self.profit = 0
        self.solutionWeight = 0