A = ['John', 'Serena', 'Bob', 'Mary', 'Serena']
B = ['Jim', 'Mary', 'John', 'Jim', 'Bob']

print('A :', A)
print('B :', B)

SA = set(A)
SB = set(B)

print('set from A :', SA)
print('set from B :', SB)

DAB = SA - SB
print('difference A\\B :', DAB)

DBA = SB - SA
print('difference B\\A :', DBA)

Diff = DAB.union(DBA)
print('symmetric difference :', Diff)