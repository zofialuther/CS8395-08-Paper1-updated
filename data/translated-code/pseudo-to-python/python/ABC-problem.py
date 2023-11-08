blocks = [("B", "O"),
          ("X", "K"),
          ("D", "Q"),
          ("C", "P"),
          ("N", "A"),
          ("G", "T"),
          ("R", "E"),
          ("T", "G"),
          ("Q", "D"),
          ("F", "S"),
          ("J", "W"),
          ("H", "U"),
          ("V", "I"),
          ("A", "N"),
          ("O", "B"),
          ("E", "R"),
          ("F", "S"),
          ("L", "Y"),
          ("P", "C"),
          ("Z", "M")]

def can_make_word(word, block_collection=blocks):
    if not word:
        return False
    blocks_remaining = list(block_collection)
    for char in word.upper():
        for block in blocks_remaining:
            if char in block:
                blocks_remaining.remove(block)
                break
        else:
            return False
    return True

import doctest
doctest.testmod()

print(", ".join("'%s': %s" % (w, can_make_word(w)) for w in
                ["", "a", "baRk", "booK", "treat",
                 "COMMON", "squad", "Confused"]))