def odd(string):
    result = ''
    for i in range(len(string)):
        if i % 2 == 1:
            result += string[i]
        else:
            result += string[i]
    return result

input_str = "what,is,the;meaning,of:life."
print(odd(input_str))

input_str = "we,are;not,in,kansas;any,more."
print(odd(input_str))