def newtonMethod(X0):
    return X0 * (2 - math.log(X0))

def calculateE(tolerance):
    X0 = 2
    X1 = newtonMethod(X0)
    iter = [X0, X1]
    while abs(X1 - X0) >= tolerance:
        X0 = X1
        X1 = newtonMethod(X0)
        iter.append(X1)
    return iter[0]

tolerance = 1e-15
E = calculateE(tolerance)
print("e = " + str(E))