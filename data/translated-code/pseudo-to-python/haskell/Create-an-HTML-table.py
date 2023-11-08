import random
import textblaze

def makeTable(headings, nRows, gen):
    table = textblaze.table()
    with table.thead():
        with table.tr():
            for heading in headings:
                table.th(heading)
        with table.tbody():
            for i in range(1, nRows+1):
                row = [i]
                for _ in range(len(headings)):
                    row.append(random.randint(1000, 9999))
                with table.tr():
                    for data in row:
                        table.td(str(data))
    return table

def main():
    headings = ["", "X", "Y", "Z"]
    gen = random.Random()
    html_table = makeTable(headings, 3, gen)
    print(html_table.render())

if __name__ == "__main__":
    main()