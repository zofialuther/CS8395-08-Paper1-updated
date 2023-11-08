def trysplit(s, delim):
    index = s.find(delim)
    if index != -1:
        return s[:index], delim, index
    else:
        return None

def multisplit(delimiters, s):
    result = []
    for delim in delimiters:
        split_result = trysplit(s, delim)
        if split_result:
            result.append(split_result)
    return result

def main():
    delimiters = [',', '.', ':']
    s = "Hello, world: Python is fun."
    results = multisplit(delimiters, s)
    for result in results:
        print(f"Substring: {result[0]}, Delimiter: {result[1]}, Offset: {result[2]}")

main()