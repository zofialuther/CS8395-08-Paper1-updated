```python
def create_ascii_table():
    ascii_table = []
    for i in range(32, 128):
        ascii_table.append(chr(i))
    return ascii_table

def format_ascii_entry(entry):
    return f"{entry:<4} {ord(entry):<5}"

def display_ascii_table(table):
    for row in table:
        print(" | ".join(row))

def main():
    ascii_table = create_ascii_table()
    formatted_table = [list(map(format_ascii_entry, ascii_table[i:i+6])) for i in range(0, len(ascii_table), 6)]
    transposed_table = list(map(list, zip(*formatted_table)))
    display_ascii_table(transposed_table)

main()
```