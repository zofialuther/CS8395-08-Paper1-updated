def directory_prefix(PATHs, STOP0, PREFIX):
    if not PATHs:
        return ''
    else:
        if longest_prefix(PATHs, STOP0, PREFIX):
            PREFIX = PREFIX + STOP0 + LONGEST_PREFIX
        else:
            PREFIX = ''
            
def longest_prefix(PATHs, STOP0, PREFIX):
    QUERY = shortest_prefix(PATHs, STOP0, SHORTEST_PREFIX)
    SHORTEST_PREFIXs = findall(SHORTEST_PREFIX, QUERY)
    LONGEST_PREFIXs = reverse(SHORTEST_PREFIXs)
    return PREFIX in LONGEST_PREFIXs

def shortest_prefix(PATHs, STOP0, PREFIX):
    if not PATHs:
        return
    else:
        if starts_with(PATH0, PREFIX) and ends_with(PREFIX, STOP0):
            shortest_prefix(PATHs, STOP0, PREFIX)

def starts_with(TARGET, START):
    return TARGET.startswith(START)

def ends_with(TARGET, END):
    return TARGET.endswith(END)