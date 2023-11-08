```python
class Transpose:
    def main(self):
        m = [[1, 2, 3], [4, 5, 6]]  # Create a 2D array
        ans = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]  # Transpose the array
        print(ans)  # Print the transposed array
```