def sort_disjoint_sublist(inputList, inputSublist):
  result = []  # initialize result variable
  # implementation of sort_disjoint_sublist function
  # ...
  return result

testCases = [
  {inputList: [7,6,5,4,3,2,1,0], inputSublist: [6,1,7], expected: [7,0,5,4,3,2,1,6]},
  {inputList: [4,2,1,4,5,5,0,0], inputSublist: [3,4,5,6,7], expected: [4,2,1,0,0,4,5,5]},
  # ... (more test cases)
]

for testCase in testCases:
  result = sort_disjoint_sublist(testCase['inputList'], testCase['inputSublist'])
  if result != testCase['expected']:
    print("Test case failed: " + str(testCase['inputList']) + ", " + str(testCase['inputSublist']))

# Run unit tests
rt()