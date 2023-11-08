ss = (
    "In olden times when wishing still helped one, there lived a king"
    "whose daughters were all beautiful, but the youngest was so beautiful"
    "that the sun itself, which has seen so much, was astonished whenever"
    "it shone in her face.  Close by the king's castle lay a great dark"
    "forest, and under an old lime-tree in the forest was a well, and when"
    "the day was very warm, the king's child went out into the forest and"
    "sat down by the side of the cool fountain, and when she was bored she"
    "took a golden ball, and threw it up on high and caught it, and this"
    "ball was her favorite plaything."
)

def wordwrap(maxlen, s):
    pos = 0
    result = ""
    words = s.split()
    for word in words:
        if pos == 0:
            result += word
            pos += len(word)
        elif pos + len(word) + 1 > maxlen:
            result += '\n' + word
            pos = len(word)
        else:
            result += ' ' + word
            pos += len(word) + 1
    return result

print(wordwrap(72, ss) + "\n" + wordwrap(32, ss))