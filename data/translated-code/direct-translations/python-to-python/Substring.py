s = 'abcdefgh'
n, m, char, chars = 2, 3, 'd', 'cd'

print(s[n-1:n+m-1])  # 'bcd'
print(s[n-1:])  # 'bcdefgh'
print(s[:-1])  # 'abcdefg'

indx = s.index(char)
print(s[indx:indx+m])  # 'def'

indx = s.index(chars)
print(s[indx:indx+m])  # 'cde'