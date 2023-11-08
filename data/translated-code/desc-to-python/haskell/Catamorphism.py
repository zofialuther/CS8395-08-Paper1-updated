```python
from Monoid import *
def main():
    numbers = [1, 2, 3, 4, 5]
    
    sum_result = foldr(Sum, numbers)
    product_result = foldr(Product, numbers)
    concat_result = foldr(Concat, numbers)
    
    print("Sum:", sum_result.get_sum())
    print("Product:", product_result.get_product())
    print("Concatenation:", concat_result.get_concatenation())
    
    strings = ["hello", "world", "python"]
    concat_strings = foldr(Concat, strings)
    print("Concatenated strings:", concat_strings.get_concatenation())
main()
```