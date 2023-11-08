def generateTriples(max):
    for coeff in [0, -1, 1]:
        count = 0
        print("Max side length " + str(max) + ", formula:  a*a + b*b " + ("" if coeff == 0 else "-" if coeff < 0 else "+") + " a*b = c*c")
        for a in range(1, max + 1):
            for b in range(1, a + 1):
                val = a*a + b*b + coeff*a*b
                c = int((val**0.5) + 0.5)
                if c > max:
                    break
                if c*c == val:
                    print("  (" + str(a) + ", " + str(b) + ", " + str(c) + ")")
                    count += 1
        print(str(count) + " triangles")

def generateTriples60(max):
    count = 0
    print("Extra Credit.")
    print("Max side length " + str(max) + ", sides different length, formula:  a*a + b*b - a*b = c*c")
    for a in range(1, max + 1):
        for b in range(1, a):
            val = a*a + b*b - a*b
            c = int((val**0.5) + 0.5)
            if c*c == val:
                count += 1
    print(str(count) + " triangles")

generateTriples(13)
generateTriples60(10000)