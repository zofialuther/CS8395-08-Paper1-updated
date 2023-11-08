gifts = '''\
A partridge in a pear tree.
Two turtle doves
Three french hens
Four calling birds
Five golden rings
Six geese a-laying
Seven swans a-swimming
Eight maids a-milking
Nine ladies dancing
Ten lords a-leaping
Eleven pipers piping
Twelve drummers drumming'''.split('\n')

days = '''first second third fourth fifth
          sixth seventh eighth ninth tenth
          eleventh twelfth'''.split()

for n in range(len(days)):
    day = days[n]
    g = gifts[:n][::-1]
    print('On the ' + day + ' day of Christmas')
    print('My true love gave to me:')
    print(' '.join(g[:-1]))
    if n > 1:
        print(' and')
    print(g[-1].capitalize())