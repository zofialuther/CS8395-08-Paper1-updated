def stripCharacters(input_string, characters_to_remove):
    for char in characters_to_remove:
        input_string = input_string.replace(char, "")
    return input_string