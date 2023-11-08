def rule90(left, center, right):
    return str(left ^ right)

def spacing(s):
    return ' ' * s

def sierpinski(iterations):
    row = '0'
    result = row + '\n'
    for i in range(iterations - 1):
        next_row = ''
        row = '0' + row + '0'
        for j in range(len(row) - 2):
            next_row += rule90(int(row[j]), int(row[j+1]), int(row[j+2]))
        result += spacing(iterations - i - 1) + next_row + '\n'
    return result

def main():
    print(sierpinski(4))