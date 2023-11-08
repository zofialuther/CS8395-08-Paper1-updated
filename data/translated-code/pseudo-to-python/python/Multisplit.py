def multisplit(text, sep):
    lastmatch = 0
    i = 0
    matches = []
    while i < len(text):
        for j, s in enumerate(sep):
            if text[i:].startswith(s):
                if i > lastmatch:
                    matches.append(text[lastmatch:i])
                matches.append((j, i))
                lastmatch = i + len(s)
                i += len(s)
                break
        if i > lastmatch:
            matches.append(text[lastmatch:i])
        i += 1
    return matches