print("Original array: ",haystack)

for needle in ("Washington","Bush"):
  try:
    index = haystack.index(needle)
    print(index, needle)
  except ValueError:
    print(needle,"is not in haystack")