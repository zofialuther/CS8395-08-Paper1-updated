```python
class Hofstadter:
    def __init__(self):
        self.Q = [0, 1]
        self.R = [0, 1]
    
    def getSequence(self, n):
        for i in range(2, n):
            self.Q.append(self.Q[i - self.Q[i-1]] + self.Q[i - self.Q[i-2]])
            self.R.append(self.R[i - self.R[i-1]] + self.R[i - self.R[i-2]])
    
    def ffr(self, n):
        return self.R[n-1]
    
    def ffs(self, n):
        return self.S[n-1]

if __name__ == "__main__":
    h = Hofstadter()
    h.getSequence(960)
    print(h.R[:10])
    setR = set(h.R[:40])
    setS = set(h.S[:960])
    both_or_neither = setR.symmetric_difference(setS)
    print(both_or_neither)
```