```python
from typing import IO
from itertools import product

def main() -> IO[None]:
    results = [print_combination(x, y, z) for x, y, z in product("abc", "ABC", "123")]

def print_combination(x, y, z) -> None:
    print(x + y + z)

if __name__ == "__main__":
    main()
```