def count_jewels(Stones, Jewels, N):
    Scodes = [ord(c) for c in Stones]
    Jcodes = [ord(c) for c in Jewels]
    SScodes = sorted(Scodes)
    SJcodes = sorted(Jcodes)
    return count_jewels_helper(SScodes, SJcodes, N, 0)

def count_jewels_helper(Stones, Jewels, N, R):
    if not Stones or not Jewels:
        return N
    if Stones[0] == Jewels[0]:
        R += 1
        return count_jewels_helper(Stones[1:], Jewels, N, R)
    elif Jewels[0] < Stones[0]:
        return count_jewels_helper(Stones, Jewels[1:], N, R)
    else:
        return count_jewels_helper(Stones[1:], Jewels, N, R)