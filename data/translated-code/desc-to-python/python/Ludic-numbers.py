```python
def ludic(max_value):
    ludic_numbers = [1] * max_value
    ludic_numbers[0] = 0
    for i in range(2, int(max_value ** 0.5) + 1):
        if ludic_numbers[i - 1] == 1:
            for j in range(i * i, max_value + 1, i):
                ludic_numbers[j - 1] = 0
    ludic_primes = [i for i in range(1, max_value) if ludic_numbers[i - 1] == 1]
    print("The first 25 Ludic primes are:", ludic_primes[:25])
    print("The count of Ludic numbers less than or equal to 1000 is:", sum(ludic_numbers[:1000]))
    print("The 2000th to 2005th Ludic primes are:", ludic_primes[1999:2005])

    triplets = [(ludic_primes[i], ludic_primes[i+1], ludic_primes[i+2]) for i in range(len(ludic_primes)-2) if ludic_primes[i] + 2 == ludic_primes[i+1] and ludic_primes[i+1] + 2 == ludic_primes[i+2]]
    print("The count of triplets of Ludic primes is:", len(triplets))
    print("The list of triplets of Ludic primes is:", triplets)

ludic(10000)
```