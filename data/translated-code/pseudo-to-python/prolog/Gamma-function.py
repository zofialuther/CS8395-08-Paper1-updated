```python
def gamma_coefficients(Cs):
    Cs = [ 1.00000000000000000000000,  0.57721566490153286060651, -0.65587807152025388107701,
      -0.04200263503409523552900,  0.16653861138229148950170, -0.04219773455554433674820,
      -0.00962197152787697356211,  0.00721894324666309954239, -0.00116516759185906511211,
      -0.00021524167411495097281,  0.00012805028238811618615, -0.00002013485478078823865,
      -0.00000125049348214267065,  0.00000113302723198169588, -0.00000020563384169776071,
       0.00000000611609510448141,  0.00000000500200764446922, -0.00000000118127457048702,
       0.00000000010434267116911,  0.00000000000778226343990, -0.00000000000369680561864,
       0.00000000000051003702874, -0.00000000000002058326053, -0.00000000000000534812253,
       0.00000000000000122677862, -0.00000000000000011812593,  0.00000000000000000118669,
       0.00000000000000000141238, -0.00000000000000000022987,  0.00000000000000000001714
    ]

def tolerance(Tol):
    Tol = 1e-17

def gamma(X, Y):
    if X <= 0.0:
        return "fail"
    elif X < 1.0:
        small_gamma(X, Y)
    elif X == 1 or X == 1.0:
        return 1
    else:
        X1 = X - 1
        gamma(X1, Y1)
        Y = X1 * Y1

def small_gamma(X, Y):
    gamma_coefficients(Cs)
    recip_gamma(X, 1.0, Cs, 1.0, 0.0, Y0)
    Y = 1 / Y0

def recip_gamma(X, PrevPow, Cs, X0, X1, Y):
    if Cs == []:
        if abs(X1 - X0) < Tol:
            Y = X1
        else:
            Y = X1
    else:
        Power = PrevPow * X
        X2 = X1 + C*Power
        recip_gamma(X, Power, Cs, X1, X2, Y)
```