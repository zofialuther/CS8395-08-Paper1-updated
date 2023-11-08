def equilibriumIndices(xs):
  leftSums = list(itertools.accumulate(xs, operator.add)) 
  rightSums = list(itertools.accumulate(xs[::-1], operator.add))[::-1]
  indices = list(range(0, len(xs)))
  result = []
  for i in range(0, len(xs)):
    if leftSums[i] == rightSums[i]:
      result.append(i)
  return result

def main():
  arrays = [ [-7, 1, 5, 2, -4, 3, 0],
            [2, 4, 6],
            [2, 9, 2],
            [1, -1, 1, -1, 1, -1, 1],
            [1],
            [] ]
  for array in arrays:
    print(equilibriumIndices(array))