```python
def y(P, Arg, R):
    Pred = P + Nb2**F2**call(P,Nb2,F2,P)
    call(Pred, Arg, R)

def test_y_combinator():
    Fib = lambda NFib: lambda RFib: lambda RFibr1: (RFib if NFib < 2 else (call(RFibr1,NFib-1,RFib1,RFibr1), call(RFibr1,NFib-2,RFib2,RFibr1), RFib is RFib1 + RFib2))
    y(Fib, 10, FR)
    print('Fib(10) = ', FR)

    Fact = lambda NFact: lambda RFact: lambda RFactr1: (RFact if NFact == 1 else (call(RFactr1,NFact-1,RFact1,RFactr1), RFact is NFact * RFact1))
    y(Fact, 10, FF)
    print('Fact(10) = ', FF)
```