```python
import math

class GammaFunction:
    def st_gamma(self, x):
        # Stirling approximation formula for gamma function
        # implementation here

    def la_gamma(self, x):
        # Lanczos approximation formula for gamma function
        # implementation here

def main():
    gamma = GammaFunction()
    for i in range(1, 11):
        result_st = gamma.st_gamma(i)
        result_la = gamma.la_gamma(i)
        print(f"Input value: {i}, Stirling method result: {result_st}, Lanczos method result: {result_la}")

if __name__ == "__main__":
    main()
```