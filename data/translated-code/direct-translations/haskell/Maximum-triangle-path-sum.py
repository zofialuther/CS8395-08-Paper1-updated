def parse(input_string):
    lines = input_string.split("\n")
    words_list = [line.split() for line in lines]
    return list(map(lambda x: list(map(int, x)), words_list))

def f(x, y, z):
    return x + max(y, z)

def g(xs, ys):
    return [f(x, y, z) for x, y, z in zip(xs, ys, ys[1:])]

def solve(parsed_input):
    result = parsed_input[0]
    for line in parsed_input[1:]:
        result = g(result, line)
    return result[0]

with open('triangle.txt', 'r') as file:
    content = file.read()
    parsed_input = parse(content)
    print(solve(parsed_input))