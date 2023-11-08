def sierpinski_carpet(n):
    def generate_carpet(size):
        if size == 1:
            return ["#"]
        else:
            smaller = generate_carpet(size // 3)
            top = [row * 3 for row in smaller]
            middle = [row + " " * (size // 3) + row for row in smaller]
            return top + middle + top

    carpet = generate_carpet(3 ** n)
    for row in carpet:
        print(row)