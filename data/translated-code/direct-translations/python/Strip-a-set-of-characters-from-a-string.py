def stripchars(s, chars):
    return "".join(c for c in s if c not in chars)

print(stripchars("She was a soul stripper. She took my heart!", "aei"))
# Output: 'Sh ws  soul strppr. Sh took my hrt!'