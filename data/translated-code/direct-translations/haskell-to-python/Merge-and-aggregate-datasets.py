```python
def tabulateDB(ps, header, cols):
    body = list(map(lambda x: "|".join(x), zip(*transpose(pad(width, table)))))
    table = list(map(lambda x: list(map(str, x)), transpose([header] + list(map(showPatient, ps))))
    width = list(map(lambda x: max(list(map(len, x))), transpose(table)))
    return body

def main():
    a = readDB(open("patients.csv").read())
    b = readDB(open("visits.csv").read())
    result = tabulateDB(a + b, header, fields)
    for line in result:
        print(line)

header = [ "PATIENT_ID", "LASTNAME", "VISIT_DATE", "SCORES SUM", "SCORES AVG"]
fields = [pid, lambda p: name(p) if name(p) else [], lambda p: visits(p)[-1] if visits(p) else [], lambda p: sum(scores(p)) if scores(p) else [], lambda p: mean(scores(p)) if scores(p) else [] ]

def mean(lst):
    return sum(lst) / len(lst)
```