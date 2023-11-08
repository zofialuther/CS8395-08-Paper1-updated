```python
class RangeExpander:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def __iter__(self):
        return self
    
    def __next__(self):
        # logic to expand the range and individual integers
        # return the next integer in the expanded sequence

class RangeExpanderTest:
    def main(self):
        input_string = "1-5,7,10-15"
        expander = RangeExpander(input_string)
        for num in expander:
            print(num)

```