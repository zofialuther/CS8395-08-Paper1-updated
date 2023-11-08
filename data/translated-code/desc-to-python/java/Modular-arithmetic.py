class ModularArithmetic:
    class ModInt:
        def __init__(self, value, modulus):
            self.value = value % modulus
            self.modulus = modulus
        
        def __add__(self, other):
            return (self.value + other.value) % self.modulus
        
        def __mul__(self, other):
            return (self.value * other.value) % self.modulus
        
        def get_value(self):
            return self.value
        
        def power(self, exponent):
            return (self.value ** exponent) % self.modulus
    
    def main():
        mod_int1 = ModularArithmetic.ModInt(5, 7)
        mod_int2 = ModularArithmetic.ModInt(3, 7)
        
        result = mod_int1 + mod_int2
        print(result)
        
    if __name__ == "__main__":
        main()