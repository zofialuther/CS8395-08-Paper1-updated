from string import ascii_uppercase

def spellWith(blocks, word):
    if not word:
        return [[]]
    else:
        return [b + rest for b in blocks for rest in spellWith([block for block in blocks if block != b], word[1:]) if word[0] in b]

def main():
    block_string = "BO XK DQ CP NA GT RE TG QD FS JW HU VI AN OB ER FS LY PC ZM"
    blocks = block_string.split()
    words = ["", "A", "BARK", "BoOK", "TrEAT", "COmMoN", "SQUAD", "conFUsE"]
    for word in words:
        print((word, not not spellWith(blocks, word.upper())))

main()