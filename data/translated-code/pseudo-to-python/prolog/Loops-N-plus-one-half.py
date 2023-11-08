def between(start, end, result):
    for i in range(start, end+1):
        result = i
        print(result, end='')
        if result < end:
            print(', ', end='')
    print()