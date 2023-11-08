```python
class AliquotSequenceClassifications:
    @staticmethod
    def properDivsSum(n):
        return sum(i for i in range(1, (n + 1) // 2 + 1) if n % i == 0 and n != i)

    @staticmethod
    def aliquot(n, maxLen, maxTerm):
        s = [n]
        newN = n
        while len(s) <= maxLen and newN < maxTerm:
            newN = AliquotSequenceClassifications.properDivsSum(s[-1])
            if newN in s:
                if s[0] == newN:
                    if len(s) == 1:
                        return AliquotSequenceClassifications.report("Perfect", s)
                    elif len(s) == 2:
                        return AliquotSequenceClassifications.report("Amicable", s)
                    else:
                        return AliquotSequenceClassifications.report("Sociable of length " + str(len(s)), s)
                elif s[-1] == newN:
                    return AliquotSequenceClassifications.report("Aspiring", s)
                else:
                    return AliquotSequenceClassifications.report("Cyclic back to " + str(newN), s)
            else:
                s.append(newN)
                if newN == 0:
                    return AliquotSequenceClassifications.report("Terminating", s)
        return AliquotSequenceClassifications.report("Non-terminating", s)

    @staticmethod
    def report(msg, result):
        print(msg + ": " + str(result))
        return False

arr = [11, 12, 28, 496, 220, 1184, 12496, 1264460, 790, 909, 562, 1064, 1488]

for n in range(1, 11):
    AliquotSequenceClassifications.aliquot(n, 16, 1 << 47)
print()
for n in arr:
    AliquotSequenceClassifications.aliquot(n, 16, 1 << 47)
```