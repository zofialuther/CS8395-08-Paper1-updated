```python
class RangeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            value = self.start
            self.start += 1
            return value
        else:
            raise StopIteration

def range_value(start, stop):
    for value in RangeIterator(start, stop):
        yield value

def calc_values(start, stop):
    values = list(range_value(start, stop))
    sum_values = sum(values)
    product_values = 1
    for value in values:
        product_values *= value
    return sum_values, product_values
```