def tabulateDB(DB, header, cols):
    body = list(zip(*cols))
    table = list(zip(header, *DB))
    width = max(map(len, table))
    return '|'.join(body)

def main():
    a = readDB(readFile("patients.csv"))
    b = readDB(readFile("visits.csv"))
    header = ["PATIENT_ID", "LASTNAME", "VISIT_DATE", "SCORES SUM", "SCORES AVG"]
    fields = [pid, fromMaybe([], name), lambda p: l[-1] if visits(p) == [] else [], lambda p: str(sum(scores(p))) if scores(p) == [] else [], lambda p: str(mean(scores(p))) if scores(p) == [] else []]
    mapM_(putStrLn, tabulateDB(a + b, header, fields))

def mean(lst):
    return sum(lst) / len(lst)