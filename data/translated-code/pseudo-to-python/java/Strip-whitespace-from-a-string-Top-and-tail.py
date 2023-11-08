string = "abc    "

def stripTrailing(input_string):
    result = ""
    i = len(input_string) - 1
    while i >= 0 and input_string[i] == " ":
        i -= 1
    result = input_string[0:i+1]
    return result

new_variable = stripTrailing(string)