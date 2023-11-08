def expandRange(input):
    result = []
    ranges = input.split(",")
    
    for num_range in ranges:
        if "--" in num_range:
            startEnd = num_range.split("--")
            start = int(startEnd[0])
            end = int(startEnd[1])
            for j in range(start, end+1):
                result.append(j)
        elif "-" in num_range:
            startEnd = num_range.split("-")
            start = int(startEnd[0])
            end = int(startEnd[1])
            for j in range(start, end+1):
                result.append(j)
        else:
            result.append(int(num_range))
    
    return result