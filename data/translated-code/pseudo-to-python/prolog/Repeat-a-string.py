from difflib import SequenceMatcher

def repeat(source, count, target):
    return repeat_helper(source, count, target)

def repeat_helper(source, count, target):
    if count == 0:
        return ''
    else:
        return source + repeat_helper(source, count-1, target)

source = "abc"
count = 3
target = ""

result = repeat(source, count, target)
print(result)