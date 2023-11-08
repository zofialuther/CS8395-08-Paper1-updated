s = 'abcdefgh'
n = 2
m = 3
char = 'd'
chars = 'cd'

substring_1 = s[n-1:n+m-1]
substring_2 = s[n-1:]
substring_3 = s[:-1]
indx_1 = s.index(char)
substring_4 = s[indx_1:indx_1+m]
indx_2 = s.index(chars)
substring_5 = s[indx_2:indx_2+m]