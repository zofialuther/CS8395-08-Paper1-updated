```python
dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", 
        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

def pointName(index):
    return dirs[index]

def pointIndex(degrees):
    index = int((degrees + 11.25) / 22.5)
    return index % 16

def printPointName(degrees):
    index = pointIndex(degrees)
    print(f"The compass point name for {degrees} degrees is {dirs[index]}")

def main():
    for i in range(32):
        print(f"{dirs[i]}: {i*11.25} degrees")

main()
```