def count_jewels(Stones, Jewels, N):
    if Stones == []:
        return N
    elif Jewels == []:
        return N
    elif Stones[0] == Jewels[0]:
        return count_jewels(Stones[1:], Jewels[1:], N+1)
    elif Jewels[0] < Stones[0]:
        return count_jewels(Stones, Jewels[1:], N)
    else:
        return count_jewels(Stones[1:], Jewels, N)

def initialize_count_jewels(Stones, Jewels, N):
    Scodes = [ord(c) for c in Stones]
    Jcodes = [ord(c) for c in Jewels]
    SScodes = msort(Scodes)
    SJcodes = sorted(Jcodes)
    count_jewels(SScodes, SJcodes, N)