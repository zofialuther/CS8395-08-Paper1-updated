class EulerIdentity:
    def main(self):
        print("e ^ (i*Pi) + 1 = " + Complex(0, math.pi).exp().add(Complex(1, 0)))

class Complex:
    def __init__(self, re, im):
        self.x = re
        self.y = im
    
    def exp(self):
        exp = math.exp(self.x)
        return Complex(exp * math.cos(self.y), exp * math.sin(self.y))
    
    def add(self, a):
        return Complex(self.x + a.x, self.y + a.y)
    
    def __str__(self):
        return str(self.x) + " + " + str(self.y) + "i"