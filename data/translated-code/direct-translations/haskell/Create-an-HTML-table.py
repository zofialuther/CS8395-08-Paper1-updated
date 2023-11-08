from random import Random, randint
import text_blaze as B

def makeTable(headings, nRows, gen):
    table = B.table()
    with table.thead:
        with B.tr:
            for heading in headings:
                B.th(heading)
        with table.tbody:
            for i in range(1, nRows + 1):
                x, gen = gen.split()
                row = B.tr()
                for j in range(len(headings)):
                    row.append(B.td(str(x)))
                    x = randint(1000, 9999)
                table.append(row)
    return table

def main():
    gen = Random()
    headings = ["", "X", "Y", "Z"]
    table = makeTable(headings, 3, gen)
    print(table.render())

if __name__ == "__main__":
    main()