```python
import random

def makeTable(headings, num_rows, rng):
    table = "<table><tr>"
    for heading in headings:
        table += f"<th>{heading}</th>"
    table += "</tr>"
    
    for _ in range(num_rows):
        table += "<tr>"
        for _ in headings:
            table += f"<td>{rng.randint(1, 10)}</td>"
        table += "</tr>"
    
    table += "</table>"
    return table

def main():
    rng = random.Random()
    headings = ["X", "Y", "Z"]
    num_rows = 3
    table = makeTable(headings, num_rows, rng)
    print(table)

if __name__ == "__main__":
    main()
```