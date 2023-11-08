```python
def dotProduct(vector1, vector2):
    if len(vector1) != len(vector2):
        return "Vector sizes differ"
    else:
        return sum(x * y for x, y in zip(vector1, vector2))

def main():
    vectors = [[1, 3, -5], [2, -1, 7], [4, 0, -2], [-3, 6, 2]]
    print("Vector         | Dot Product")
    print("-----------------------------")
    for vector in vectors:
        result = dotProduct([1, 3, -5], vector)
        print(f"{vector} | {result}")

if __name__ == "__main__":
    main()
```