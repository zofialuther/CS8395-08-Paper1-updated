def disSort1(xs, is):
  is_ = sorted(is)
  sub_rest = partition(lambda x: x[1] in is_, enumerate(xs))
  sub = [x for x in sub_rest if x[1] in is_]
  rest = [x for x in sub_rest if x[1] not in is_]
  result = [x[1] for x in sorted(sub, key=lambda x: is_.index(x[1]))] + [x[1] for x in sorted(rest, key=lambda x: x[0])]
  return result

def disSort2(xs, is):
  as_ = {i:xs[i] for i in range(len(xs))}
  sub = [(is[i], as_[i]) for i in range(len(is))]
  sub.sort(key=lambda x: x[0])
  result = [x[1] for x in sub]
  return result

def disSort3(xs, is):
  as_ = {i:xs[i] for i in range(len(xs))}
  sub = [(is[i], as_[i]) for i in range(len(is))]
  sub.sort(key=lambda x: x[0])
  result = [x[1] for x in sub]
  return result

def main():
  xs = [7, 6, 5, 4, 3, 2, 1, 0]
  is = [6, 1, 7]
  print(disSort1(xs, is))
  print(disSort2(xs, is))
  print(disSort3(xs, is))