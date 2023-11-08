def brace_expansion(input_string, Out):
    if "{" not in input_string:
        Out.append(input_string)
    else:
        start = input_string.find("{")
        end = input_string.find("}")
        options = input_string[start+1:end].split(",")
        for option in options:
            new_string = input_string[:start] + option + input_string[end+1:]
            brace_expansion(new_string, Out)
    return Out