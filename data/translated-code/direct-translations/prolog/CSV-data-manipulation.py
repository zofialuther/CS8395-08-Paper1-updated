```python
def test():
    augment('test.csv', 'test.out.csv')

def augment(InFileName, OutFileName):
    with open(OutFileName, 'w') as OutStream:
        with open(InFileName, 'r') as InFile:
            for row in csv.reader(InFile):
                if row[0].isdigit():
                    row.append(sum(int(i) for i in row))
                else:
                    row.append('SUM')
                csv.writer(OutStream).writerow(row)
```