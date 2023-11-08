def joins(left, right):
    return left[-1] == right[0]

def exampleBind():
    result = []
    words1 = ["the", "that", "a"]
    for w1 in words1:
        words2 = ["frog", "elephant", "thing"]
        for w2 in words2:
            words3 = ["walked", "treaded", "grows"]
            for w3 in words3:
                words4 = ["slowly", "quickly"]
                for w4 in words4:
                    if joins(w1, w2) and joins(w2, w3) and joins(w3, w4):
                        result.append(f"{w1} {w2} {w3} {w4}")
    return ' '.join(result)

def exampleConcatMap():
    words1 = ["the", "that", "a"]
    return ' '.join([f"{w1} {w2} {w3} {w4}" for w1 in words1 for w2 in ["frog", "elephant", "thing"] for w3 in ["walked", "treaded", "grows"] for w4 in ["slowly", "quickly"] if joins(w1, w2) and joins(w2, w3) and joins(w3, w4)])

def main():
    print(exampleBind())
    print(exampleConcatMap())

main()