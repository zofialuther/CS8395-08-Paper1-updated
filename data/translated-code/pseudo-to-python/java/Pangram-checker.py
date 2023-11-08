def isPangram(test):
    for a in range(ord('A'), ord('Z')+1):
        if chr(a) not in test and chr(a+32) not in test:
            return False
    return True

def main(args):
    print(isPangram("the quick brown fox jumps over the lazy dog")) #true
    print(isPangram("the quick brown fox jumped over the lazy dog")) #false, no s
    print(isPangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) #true
    print(isPangram("ABCDEFGHIJKLMNOPQSTUVWXYZ")) #false, no r
    print(isPangram("ABCDEFGHIJKL.NOPQRSTUVWXYZ")) #false, no m
    print(isPangram("ABC.D.E.FGHI*J/KL-M+NO*PQ R\nSTUVWXYZ")) #true
    print(isPangram("")) #false