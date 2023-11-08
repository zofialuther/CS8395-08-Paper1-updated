```python
import Data.List
import HFM.Primes
import Control.Monad
import Control.Arrow

smallest_prime_factor :: Int -> Int
smallest_prime_factor n = head $ filter (\x -> n `mod` x == 0) $ takeWhile (\x -> x*x <= n) primes
```