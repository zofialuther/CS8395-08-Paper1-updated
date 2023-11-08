from typing import Callable

def Y(f: Callable[[Callable], Callable]) -> Callable:
    class RecursiveFunction:
        def __call__(self, w):
            return f(lambda x: w(w)(x))
    
    r = RecursiveFunction()
    return r(r)

if __name__ == "__main__":
    fib = Y(lambda f: lambda n: 1 if n <= 2 else f(n - 1) + f(n - 2))
    fac = Y(lambda f: lambda n: 1 if n <= 1 else n * f(n - 1))

    print("fib(10) = ", fib(10))
    print("fac(10) = ", fac(10))