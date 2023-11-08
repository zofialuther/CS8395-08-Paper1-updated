def church_zero(z):
    return z

def church_successor(Z):
    return "c(" + str(Z) + ")"

def church_add(z, Z):
    return Z

def church_add(c(X), Y):
    return "c(" + str(X + Y) + ")"

def church_multiply(z, _):
    return z

def church_multiply(c(X), Y):
    return church_add(Y, church_multiply(X, Y))

def church_power(z, z):
    return z

def church_power(N, c(z)):
    return N

def church_power(N, c(c(Z))):
    return church_multiply(N, church_power(N, c(Z)))

def int_church(I, Z):
    if I == 0:
        return Z
    else:
        return "c(" + str(int_church(I-1, Z)) + ")"

def run():
    Three = int_church(3, "z")
    Four = church_successor(Three)
    Sum = church_add(Three, Four)
    Product = church_multiply(Three, Four)
    Power43 = church_power(Four, Three)
    Power34 = church_power(Three, Four)

    ISum = int_church(3, Sum)
    IProduct = int_church(3, Product)
    IPower43 = int_church(3, Power43)
    IPower34 = int_church(3, Power34)

    print(ISum, IProduct, IPower43, IPower34)