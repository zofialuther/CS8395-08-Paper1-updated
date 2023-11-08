def factors(pairs):
    for i in range(1, 101):
        output = ""
        for factor, word in pairs:
            if i % factor == 0:
                output += word
        if output:
            print(output)
        else:
            print(i)

factors([(3, "Fizz"), (5, "Buzz")])