```python
def church_zero(z):
    return z

def church_successor(Z):
    return f'c({Z})'

def church_add(z, Z, result):
    result = Z

def church_add(c_X, Y, result):
    Z = f'c({result})'
    return Z

def church_multiply(z, Y, result):
    result = z

def church_multiply(c_X, Y, result):
    S = result
    R = f'c({S})'
    return R

def church_power(N, z, result):
    result = z

def church_power(N, c_z, result):
    result = N

def church_power(N, c_c_Z, result):
    R1 = result
    R = f'c({R1})'
    return R

def int_church(I, z):
    I = 0

def int_church(I, c_Z):
    Is = I
    return Is + 1

def run():
    Three = int_church(3, z)
    Four = church_successor(Three)
    Sum = church_add(Three, Four)
    Product = church_multiply(Three, Four)
    Power43 = church_power(Four, Three)
    Power34 = church_power(Three, Four)

    ISum = int_church(Sum)
    IProduct = int_church(Product)
    IPower43 = int_church(Power43)
    IPower34 = int_church(Power34)

    print(ISum, IProduct, IPower43, IPower34)

run()
```