class EulerIdentity:
    def __init__(self):
        pass
    
    @staticmethod
    def main(args):
        complex_num = Complex(0, math.pi).exp().add(Complex(1, 0))
        print("e ^ (i*Pi) + 1 = " + str(complex_num))

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