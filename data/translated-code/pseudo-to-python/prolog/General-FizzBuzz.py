def factors(array):
    for i in range(1, 101):
        output = ""
        for pair in array:
            if i % pair[0] == 0:
                output += pair[1]
        if output == "":
            output = i
        print(output)