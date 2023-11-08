def maxnum(x):
    maxlen = len(str(max(x)))
    sorted_numbers = sorted(x, key=lambda i: i * (maxlen * 2) // len(str(i)), reverse=True)
    return ''.join(map(str, sorted_numbers))

for numbers in [(212, 21221), (1, 34, 3, 98, 9, 76, 45, 4), (54, 546, 548, 60)]:
    print('Numbers: %r\n  Largest integer: %15s' % (numbers, maxnum(numbers)))