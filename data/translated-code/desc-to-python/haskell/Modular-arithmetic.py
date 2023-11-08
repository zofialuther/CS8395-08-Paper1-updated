```python
{-# LANGUAGE TypeOperators #-}
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE TypeFamilies #-}

import Data.Modular

type family (a :: Z) / (b :: Z) :: Z

type instance a / b = a * recip b

f :: Z / 13 -> Z / 13
f x = (x ^ (100 :: Z)) + x + 1

main :: IO ()
main = print $ f (10 :: Z / 13)
```