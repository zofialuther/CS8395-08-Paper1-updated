emp = [
    ('Tyler Bennett','E10297',32000,'D101'),
    ('John Rappl','E21437',47000,'D050'),
    ('George Woltman','E00127',53500,'D101'),
    ('Adam Smith','E63535',18000,'D202'),
    ('Claire Buckman','E39876',27800,'D202'),
    ('David McClellan','E04242',41500,'D101'),
    ('Rich Holcomb','E01234',49500,'D202'),
    ('Nathan Adams','E41298',21900,'D050'),
    ('Richard Potter','E43128',15900,'D101'),
    ('David Motsinger','E27002',19250,'D202'),
    ('Tim Sampair','E03033',27000,'D101'),
    ('Kim Arlich','E10001',57000,'D190'),
    ('Timothy Grove','E16398',29900,'D190')
]

def departments():
    DList = [e[3] for e in emp]
    return list(set(DList))

def greater(emp1, emp2):
    return emp1[2] > emp2[2]

def topSalary(N, Emp, R):
    if N == 0:
        return []
    if not R:
        return [Emp]
    if greater(Emp, R[0]):
        return [Emp] + topSalary(N-1, R[0], R[1:])
    else:
        return [R[0]] + topSalary(N-1, Emp, R[1:])

def topEmps(N, Emps, R):
    if not Emps:
        return R
    Rt = topSalary(N, Emps[0], R)
    return topEmps(N, Emps[1:], Rt)

def topDeps(N):
    D = departments()
    Res = topDepsHelper(N, D)
    for dept, topEmps in Res:
        print(f"Department: {dept}")
        for emp in topEmps:
            print(f"  ID: {emp[1]}\t{emp[0]}\tSalary: {emp[2]}")

def topDepsHelper(N, D):
    res = []
    for dept in D:
        Emps = [e for e in emp if e[3] == dept]
        topEmps = topEmps(N, Emps, [])
        res.append((dept, topEmps))
    return res

topDeps(3)