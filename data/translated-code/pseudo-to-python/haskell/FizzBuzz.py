def main():
  fizzBuzzList = generateFizzBuzzList()
  numbers = generateNumbers()
  
  for i in range(100):
    if fizzBuzzList[i] != "":
      print(fizzBuzzList[i])
    else:
      print(numbers[i])

def generateFizzBuzzList():
  fizzList = ["", "", "Fizz"]
  buzzList = ["", "", "", "", "Buzz"]
  result = []
  
  for i in range(100):
    result.append(fizzList[i % len(fizzList)] + buzzList[i % len(buzzList)])
  
  return result

def generateNumbers():
  result = []
  
  for i in range(1, 101):
    result.append(str(i))
  
  return result

main()