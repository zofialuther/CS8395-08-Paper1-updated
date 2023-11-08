```python
class PartialApplication:
    class IntegerFunction:
        def call(self, arg):
            pass
    
    @staticmethod
    def fs(f, s):
        r = []
        for i in range(len(s)):
            r.append(f.call(s[i]))
        return r
    
    class SequenceFunction:
        def call(self, arg):
            pass
    
    @staticmethod
    def fs(f):
        class InnerSequenceFunction:
            def call(self, s):
                return PartialApplication.fs(f, s)
        return InnerSequenceFunction()
    
    f1 = PartialApplication.IntegerFunction()
    f2 = PartialApplication.IntegerFunction()
    
    f1.call = lambda i: i * 2
    f2.call = lambda i: i * i
    
    fsf1 = PartialApplication.fs(f1)
    fsf2 = PartialApplication.fs(f2)
    
    sequences = [
        [0, 1, 2, 3],
        [2, 4, 6, 8]
    ]
    
    for array in sequences:
        print(f"array: {array}")
        print(f"  fsf1(array): {fsf1.call(array)}")
        print(f"  fsf2(array): {fsf2.call(array)}")
```