```python
# Implements the American soundex algorithm
# as described at https://en.wikipedia.org/wiki/Soundex
# In SWI Prolog, a 'string' is specified in 'single quotes',
# while a "list of codes" may be specified in "double quotes".
# So, "abc" is equivalent to [97, 98, 99], while
# 'abc' = abc  (an atom), and 'Abc' is also an atom.  There are
# conversion methods that can produce lists of characters:
#        ?- atom_chars('Abc', X).
#	 X = ['A', b, c].
#    or lists of codes (mapping to unicode code points):
#        ?- atom_codes('Abc', X).
#        X = [65, 98, 99].
#    and the conversion predicates are bidirectional.
#        ?- atom_codes(A, [65, 98, 99]).
#        A = 'Abc'.
#  A single character code may be specified as 0'C, where C is the
#    character you want to convert to a code.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Relates groups of consonants to representative digits
def creplace(Ch, result):
    if Ch in "bfpv":
        result = '1'
    elif Ch in "cgjkqsxz":
        result = '2'
    elif Ch in "dt":
        result = '3'
    elif Ch == 'l':
        result = '4'
    elif Ch in "mn":
        result = '5'
    elif Ch == 'r':
        result = '6'
    return result

# strips elements contained in <Set> from a string
def strip(Set, string):
    result = ''.join([char for char in string if char not in Set])
    return result

# Replace consonants with appropriate digits
def consonants(string):
    result = ''.join([creplace(char) for char in string])
    return result

# Replace adjacent digits with single digit
def adjacent(string):
    result = ''
    i = 0
    while i < len(string):
        if string[i] == string[i+1]:
            result += string[i]
            i += 2
        else:
            result += string[i]
            i += 1
    return result

# Replace first character with original one if its a digit
def chk_digit(string):
    result = string
    if string[1].isdigit():
        result = string[0] + string[2:]
    return result

# Faithful representation of soundex rules:
#   1: Save 1st letter, strip "hw"
#   2: Replace consonants with appropriate digits
#   3: Replace adjacent digits with single occurrence
#   4: Remove vowels except 1st letter
#   5: If 1st symbol is a digit, replace it with saved 1st letter
#   6: Ensure trailing zeroes
def do_soundex(Text):
    T = Text.lower()
    T = T.replace('hw', '')
    T = consonants(T)
    T = adjacent(T)
    T = T.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').replace('y', '')
    T = chk_digit(T)
    T += '0000'
    result = T[:4]
    return result

# Prepare string, convert to lower case and do the soundex algorithm
def soundex(Text):
    return do_soundex(Text)

# Perform tests to check that the right values are produced
def test():
    tests = {
        'Robert': 'r163', 
        'Rupert': 'r163', 
        'Rubin': 'r150', 
        'Ashcroft': 'a261', 
        'Ashcraft': 'a261', 
        'Tymczak': 't522', 
        'Pfister': 'p236'
    }
    for key, value in tests.items():
        if soundex(key) != value:
            print(f"{key} failed")
            return
    print("All tests passed")

test()
```