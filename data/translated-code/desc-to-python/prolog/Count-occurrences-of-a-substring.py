def count_substring(string, substring):
    if len(string) < len(substring):
        return 0
    elif string[:len(substring)] == substring:
        return 1 + count_substring(string[len(substring):], substring)
    else:
        return count_substring(string[1:], substring)

def substring_rest(string, substring):
    if len(string) < len(substring):
        return ""
    elif string[:len(substring)] == substring:
        return string[len(substring):]
    else:
        return substring_rest(string[1:], substring)