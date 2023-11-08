```python
def generateTable():
    tableData = []
    header = ["", "X", "Y", "Z"]
    tableData.append(header)
    
    for i in range(rows): 
        row = []
        row.append(i)
        row.append(X[i])
        row.append(Y[i])
        row.append(Z[i])
        tableData.append(row)

    return tableData
```