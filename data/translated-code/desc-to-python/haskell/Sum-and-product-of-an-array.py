import Data.Array

# Create an array containing the numbers 11 to 20
arr = Data.Array.listArray (1, [11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

# Apply sum function to the elements of the array
sum_result = Data.Array.sum arr

# Apply product function to the elements of the array
product_result = Data.Array.product arr

# Apply print function to the results
Data.Array.mapM_ print [sum_result, product_result]