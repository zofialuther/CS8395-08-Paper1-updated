```python
def fizzEtc(rules, n):
    result = []
    for i in range(1, n+1):
        temp = ""
        for r in rules:
            if i % r[0] == 0:
                temp += r[1]
        if temp == "":
            temp = str(i)
        result.append(temp)
    return result

def main():
    rules = [(3, "Fizz"), (5, "Buzz"), (7, "Baxx")]
    result = fizzEtc(rules, 20)
    print(result)

if __name__ == "__main__":
    main()
```