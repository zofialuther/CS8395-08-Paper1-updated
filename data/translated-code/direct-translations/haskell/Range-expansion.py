def expandRange(input_string):
    numbers = input_string.split(',')
    result = []
    for number in numbers:
        if '-' in number:
            start, end = number.split('-')
            for i in range(int(start), int(end) + 1):
                result.append(i)
        else:
            result.append(int(number))
    return result

print(expandRange("-6,-3--1,3-5,7-11,14,15,17-20"))