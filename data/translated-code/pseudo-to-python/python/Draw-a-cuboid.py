def _pr(t, x, y, z):
    txt = ''
    for m in range(3+y+z-1, -1, -1):
        line = ''
        for n in range(3+x+z):
            line = line + t[(n, m)]
        txt = txt + line.strip() + '\n'
    return txt

def cuboid(x, y, z):
    t = {}
    for n in range(3+x+z):
        for m in range(3+y+z):
            t[(n,m)] = ' '
    
    xrow = ['+']
    for i in range(x):
        xrow = xrow + '%i' % (i % 10)
    xrow = xrow + ['+']
    for i, ch in enumerate(xrow):
        t[(i,0)] = ch
        t[(i,1+y)] = ch
        t[(1+z+i,2+y+z)] = ch
    
    if _debug:
        print(_pr(t, x, y, z))
    
    ycol = ['+']
    for j in range(y):
        ycol = ycol + '%i' % (j % 10)
    ycol = ycol + ['+']
    for j, ch in enumerate(ycol):
        t[(0,j)] = ch
        t[(x+1,j)] = ch
        t[(2+x+z,1+z+j)] = ch
    
    if _debug:
        print(_pr(t, x, y, z))
    
    zdepth = ['+']
    for k in range(z):
        zdepth = zdepth + '%i' % (k % 10)
    zdepth = zdepth + ['+']
    for k, ch in enumerate(zdepth):
        t[(k,1+y+k)] = ch
        t[(1+x+k,1+y+k)] = ch
        t[(1+x+k,k)] = ch
    
    return _pr(t, x, y, z)

_debug = False
if __name__ == '__main__':
    for dim in ((2,3,4), (3,4,2), (4,2,3)):
        print("CUBOID%r" % (dim,), cuboid(*dim), sep='\n')