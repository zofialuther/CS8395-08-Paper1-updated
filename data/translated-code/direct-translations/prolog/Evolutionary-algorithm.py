```python
import random

def rndAlpha(*args):
    if len(args) == 2:
        return chr(random.randint(args[0], args[1]))
    else:
        n = random.random()
        p = int(64 + (n * 27))
        return chr(p)

def rndTxt(Len):
    return [rndAlpha(64, 90) for _ in range(Len)]

def score(Txt, Target):
    score = 0
    for i in range(len(Target)):
        if Txt[i] != Target[i]:
            score += 1
    return score

def mutate(P, Txt):
    mutated = []
    for char in Txt:
        if random.random() < P:
            mutated.append(rndAlpha(64, 90))
        else:
            mutated.append(char)
    return mutated

def weasel(Tries, Chance, Target, Start):
    while True:
        score_and_mutations = []
        for _ in range(30):
            mutated = mutate(Chance, Start)
            s = score(mutated, Target)
            score_and_mutations.append((s, mutated))
        
        score_and_mutations.sort(key=lambda x: x[0])
        best_score, best_mutation = score_and_mutations[0]

        Tries += 1
        if best_score == 0:
            print(f"{Tries}: {best_score} - {''.join(best_mutation)}")
            return
        else:
            print(f"{Tries}: {best_score} - {''.join(best_mutation)}")
            Start = best_mutation

weasel(0, 1 - (1/(len("METHINKS IT IS LIKE A WEASEL")+1)), list("METHINKS IT IS LIKE A WEASEL"), rndTxt(len("METHINKS IT IS LIKE A WEASEL")))
```