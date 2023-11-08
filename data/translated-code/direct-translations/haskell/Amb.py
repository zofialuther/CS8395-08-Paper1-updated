def joins(left, right):
    return left[-1] == right[0]

exampleBind = [w1 + " " + w2 + " " + w3 + " " + w4
               for w1 in ["the", "that", "a"]
               for w2 in ["frog", "elephant", "thing"]
               for w3 in ["walked", "treaded", "grows"]
               for w4 in ["slowly", "quickly"]
               if joins(w1, w2) and joins(w2, w3) and joins(w3, w4)]

exampleConcatMap = [w1 + " " + w2 + " " + w3 + " " + w4
                    for w1 in ["the", "that", "a"]
                    for w2 in ["frog", "elephant", "thing"]
                    for w3 in ["walked", "treaded", "grows"]
                    for w4 in ["slowly", "quickly"]
                    if joins(w1, w2) and joins(w2, w3) and joins(w3, w4)]

print(exampleBind)
print(exampleConcatMap)