def word_wrap(String, Length, Wrapped):
    Words = String.split("\\S+")
    wrap(Words, Length, Length, Wrapped, '')

def wrap([_], _, _, Result, Result):
    return

def wrap([Space, Word, *Words], Line_length, Space_left, Result, String):
    Word_len = len(Word)
    Space_len = len(Space)
    if Space_left < Word_len + Space_len:
        Space1 = '\n'
        Space_left1 = Line_length - Word_len
    else:
        Space1 = Space
        Space_left1 = Space_left - Word_len - Space_len
    String1 = String + Space1 + Word
    wrap(Words, Line_length, Space_left1, Result, String1)

sample_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def test_word_wrap(Line_length):
    Text = sample_text
    Wrapped = word_wrap(Text, Line_length)
    print('Wrapped at ' + str(Line_length) + ' characters:\n' + Wrapped)

def main():
    test_word_wrap(60)
    print('\n')
    test_word_wrap(80)