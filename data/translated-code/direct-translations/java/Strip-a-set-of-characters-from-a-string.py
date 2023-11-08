def stripCharacters(string, characters):
    for character in characters:
        string = string.replace(character, "")
    return string