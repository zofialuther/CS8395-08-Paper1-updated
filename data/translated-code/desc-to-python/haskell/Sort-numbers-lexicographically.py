import Data.List

main = do
  let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  let sortedNumbers = sortOn show numbers
  print sortedNumbers