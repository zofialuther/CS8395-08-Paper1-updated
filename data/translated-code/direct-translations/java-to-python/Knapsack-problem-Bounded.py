```python
from typing import List
from hu.pj.obj import Item

class ZeroOneKnapsack:
    def __init__(self, maxWeight: int = 0, itemList: List[Item] = []):
        self.itemList = itemList
        self.maxWeight = maxWeight
        self.solutionWeight = 0
        self.profit = 0
        self.calculated = False

    def calcSolution(self) -> List[Item]:
        n = len(self.itemList)

        self.setInitialStateForCalculation()
        if n > 0 and self.maxWeight > 0:
            c = [[] for _ in range(n + 1)]
            curr = [0] * (self.maxWeight + 1)
            c[0] = curr
            for j in range(self.maxWeight + 1):
                curr[j] = 0
            for i in range(1, n + 1):
                prev = curr
                c[i] = curr = [0] * (self.maxWeight + 1)
                for j in range(self.maxWeight + 1):
                    if j > 0:
                        wH = self.itemList[i-1].getWeight()
                        curr[j] = prev[j] if wH > j else max(prev[j], self.itemList[i-1].getValue() + prev[j - wH])
                    else:
                        curr[j] = 0
            self.profit = curr[self.maxWeight]

            i, j = n, self.maxWeight
            while i > 0 and j >= 0:
                tempI = c[i][j]
                tempI_1 = c[i-1][j]
                if (i == 0 and tempI > 0) or (i > 0 and tempI != tempI_1):
                    iH = self.itemList[i-1]
                    wH = iH.getWeight()
                    iH.setInKnapsack(1)
                    j -= wH
                    self.solutionWeight += wH
                i -= 1
            self.calculated = True
        return self.itemList

    def add(self, name: str, weight: int, value: int):
        if name == "":
            name = str(len(self.itemList) + 1)
        self.itemList.append(Item(name, weight, value))
        self.setInitialStateForCalculation()

    def remove(self, name: str):
        self.itemList = [item for item in self.itemList if item.getName() != name]
        self.setInitialStateForCalculation()

    def removeAllItems(self):
        self.itemList.clear()
        self.setInitialStateForCalculation()

    def getProfit(self) -> int:
        if not self.calculated:
            self.calcSolution()
        return self.profit

    def getSolutionWeight(self) -> int:
        return self.solutionWeight

    def isCalculated(self) -> bool:
        return self.calculated

    def getMaxWeight(self) -> int:
        return self.maxWeight

    def setMaxWeight(self, maxWeight: int):
        self.maxWeight = max(maxWeight, 0)

    def setItemList(self, itemList: List[Item]):
        if itemList is not None:
            self.itemList = itemList
            for item in itemList:
                item.checkMembers()

    def setInKnapsackByAll(self, inKnapsack: int):
        for item in self.itemList:
            item.setInKnapsack(1) if inKnapsack > 0 else item.setInKnapsack(0)

    def setInitialStateForCalculation(self):
        self.setInKnapsackByAll(0)
        self.calculated = False
        self.profit = 0
        self.solutionWeight = 0
```