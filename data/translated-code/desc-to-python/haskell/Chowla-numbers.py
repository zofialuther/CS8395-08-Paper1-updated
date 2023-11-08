```python
import multiprocessing

def chowla_function(n):
    # code to calculate Chowla function for a given number
    pass

def count_primes_and_perfect_numbers(start, end):
    # code to count primes and perfect numbers within specified range
    pass

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_cores)

    # execute chowla_function and count_primes_and_perfect_numbers using parallel processing
    # print the results with informative messages
```