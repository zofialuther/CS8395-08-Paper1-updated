class GammaFunction:
    def st_gamma(self, x):
        return sqrt(2 * PI / x) * pow((x / E), x)

    def la_gamma(self, x):
        p = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
             771.32342877765313, -176.61502916214059, 12.507343278686905,
             -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7]
        g = 7
        if x < 0.5:
            return PI / (sin(PI * x) * self.la_gamma(1 - x))

        x -= 1
        a = p[0]
        t = x + g + 0.5
        for i in range(1, len(p)):
            a += p[i] / (x + i)
        
        return sqrt(2 * PI) * pow(t, x + 0.5) * exp(-t) * a

    def main(self, args):
        test = GammaFunction()
        print("Gamma \t\tStirling \t\tLanczos")
        for i in range(1, 21):
            print(i / 10.0, "\t\t", test.st_gamma(i / 10.0), "\t", test.la_gamma(i / 10.0))