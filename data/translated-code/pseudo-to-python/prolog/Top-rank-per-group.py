```python
def emp(name,id,salary,dpt):
  employees = [
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

def departments(Depts):
  DList = [emp for emp in employees if emp[3] == Depts]
  Depts = set(DList)

def greater(emp1, emp2):
  return emp1[2] > emp2[2]

def topSalary(N, Emp, R, Res):
  if N == 0:
    return
  if greater(Emp, R[0]) and N > 0:
    N0 = N - 1
    topSalary(N0, R[0], R[1:], [Emp]+Res)
  elif N > 0:
    N0 = N - 1
    topSalary(N0, Emp, R[1:], Res)

def topEmps(N, Emps, R, Res):
  topSalary(N, Emps[0], R, Rt)
  topEmps(N, Emps[1:], Rt, [Emps[0]]+Res)

def topDeps(N, T, Res):
  Dept = T[0]
  Emps = [emp for emp in employees if emp[3] == Dept]
  Ro = []
  topEmps(N, Emps, [], Ro)
  Res.append((Dept,Ro))
  topDeps(N, T[1:], Res)

def topDeps(N):
  departments(D)
  Res = []
  topDeps(N, D, Res)
  for dept, R in Res:
    print('Department:', dept)
    for emp in R:
      print('  ID:', emp[1], '\t', 'Name:', emp[0], '\t', 'Salary:', emp[2])
```