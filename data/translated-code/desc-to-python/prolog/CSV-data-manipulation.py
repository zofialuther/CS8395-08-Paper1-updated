```python
import csv

def augment(input_file, output_file):
    with open(output_file, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        with open(input_file, 'r', newline='') as in_file:
            reader = csv.reader(in_file)
            for row in reader:
                if row[0].isdigit():
                    row.append(sum(map(int, row)))
                else:
                    row.append('SUM')
                writer.writerow(row)

def test():
    augment('test.csv', 'test.out.csv')

test()
```