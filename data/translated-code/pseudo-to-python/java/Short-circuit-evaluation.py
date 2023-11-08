def main(args):
    print("F and F = " + str(a(False) and b(False)) + "\n")
    print("F or F = " + str(a(False) or b(False)) + "\n")

    print("F and T = " + str(a(False) and b(True)) + "\n")
    print("F or T = " + str(a(False) or b(True)) + "\n")

    print("T and F = " + str(a(True) and b(False)) + "\n")
    print("T or F = " + str(a(True) or b(False)) + "\n")

    print("T and T = " + str(a(True) and b(True)) + "\n")
    print("T or T = " + str(a(True) or b(True)) + "\n")

def a(a):
    print("a")
    return a

def b(b):
    print("b")
    return b