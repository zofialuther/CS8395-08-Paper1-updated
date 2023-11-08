class FuscSequence:
    FUSC_MAX = 30000000
    fusc = [0] * FUSC_MAX
    
    @staticmethod
    def main():
        print("Show the first 61 fusc numbers (starting at zero) in a horizontal format")
        for n in range(61):
            print("{}, ".format(FuscSequence.fusc[n]), end="")
        
        print("\n\nShow the fusc number (and its index) whose length is greater than any previous fusc number length.")
        start = 0
        for i in range(6):
            val = 10**i if i != 0 else -1
            for j in range(start, FuscSequence.FUSC_MAX):
                if FuscSequence.fusc[j] > val:
                    print("fusc[{}] = {}".format(j, FuscSequence.fusc[j]))
                    start = j
                    break
    
    @staticmethod
    def generate_fusc_sequence():
        FuscSequence.fusc[0] = 0
        FuscSequence.fusc[1] = 1
        for n in range(2, FuscSequence.FUSC_MAX):
            FuscSequence.fusc[n] = FuscSequence.fusc[n//2] if n % 2 == 0 else FuscSequence.fusc[(n-1)//2] + FuscSequence.fusc[(n+1)//2]

FuscSequence.generate_fusc_sequence()
FuscSequence.main()
