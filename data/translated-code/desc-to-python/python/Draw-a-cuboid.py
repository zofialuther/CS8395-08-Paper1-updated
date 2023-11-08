def cuboid(length, width, height):
    result = ""
    for i in range(height):
        result += "\n" + _pr(length, width, height, i)
    return result

def _pr(length, width, height, i):
    result = ""
    for j in range(length):
        result += "+"
    result += "\n"
    for j in range(width):
        result += "|"
        for k in range(length):
            result += " "
        result += "|\n"
    result += "+"
    for j in range(length):
        result += "-"
    result += "+"
    return result

if __name__ == "__main__":
    debug_mode = True
    if debug_mode:
        print(cuboid(3, 4, 5))
        print(cuboid(2, 2, 2))
        print(cuboid(5, 3, 7))