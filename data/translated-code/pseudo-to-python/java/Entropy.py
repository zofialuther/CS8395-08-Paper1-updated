import math

class REntropy:
    def getShannonEntropy(s):
        n = 0
        occ = {}

        for c_ in range(len(s)):
            cx = s[c_]
            if cx in occ:
                occ[cx] += 1
            else:
                occ[cx] = 1
            n += 1

        e = 0.0
        for key, value in occ.items():
            p = value / n
            e += p * math.log2(p)

        return -e

    def log2(a):
        return math.log(a) / math.log(2)

    def main(args):
        sstr = ["1223334444", "1223334444555555555", "122333", "1227774444", "aaBBcccDDDD", "1234567890abcdefghijklmnopqrstuvwxyz", "Rosetta Code"]

        for ss in sstr:
            entropy = REntropy.getShannonEntropy(ss)
            print("Shannon entropy of " + ss + ": " + str(entropy))