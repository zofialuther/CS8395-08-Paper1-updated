```python
class AccumulatorFactory:
    
    @staticmethod
    def create_accumulator():
        total = 0
        
        def accumulator(input_num):
            nonlocal total
            total += input_num
            return total
        
        return accumulator

if __name__ == "__main__":
    accumulator = AccumulatorFactory.create_accumulator()
    
    print(accumulator(5))
    print(accumulator(10))
    print(accumulator(3.5))
    print(accumulator(2.5))
```