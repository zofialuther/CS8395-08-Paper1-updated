def main():
  words = [
    ["the", "that", "a"],
    ["frog", "elephant", "thing"],
    ["walked", "treaded", "grows"],
    ["slowly", "quickly"]
  ]
  print(amb(words))

def amb(aOptions):
  continues = lambda before, after: before.endswith(after[0])
  ambResult = amb(continues, aOptions, "")
  if not ambResult:
    return "No match found"
  else:
    return " ".join(ambResult)

def amb(aBiFunction, aOptions, aPrevious):
  if not aOptions:
    return []

  for option in aOptions[0]:
    if aPrevious and not aBiFunction(aPrevious, option):
      continue
    if len(aOptions) == 1:
      return [option]
    result = amb(aBiFunction, aOptions[1:], option)
    if result:
      result.insert(0, option)
      return result

  return []