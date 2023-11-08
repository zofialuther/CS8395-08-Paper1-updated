```python
# Define the PythagComp interface
class PythagComp:
    # Define the main method
    @staticmethod
    def main(*args):
        # Print the result of the run method with input 20
        print(PythagComp.run(20))

    # Define the run method with input parameter n
    @staticmethod
    def run(n):
        result = []
        # Use range to create a stream of integers from 1 to n
        for x in range(1, n):
            for y in range(x, n):
                for z in range(y, n):
                    # For each z in the third stream, create a new Integer array with x, y, and z
                    if x * x + y * y == z * z:
                        result.append([x, y, z])
        return result
```