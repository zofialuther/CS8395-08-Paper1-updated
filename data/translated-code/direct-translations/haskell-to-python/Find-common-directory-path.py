```python
from itertools import groupby

# Return the common prefix of two lists.
def commonPrefix2(xs, ys):
    if xs and ys and xs[0] == ys[0]:
        return [xs[0]] + commonPrefix2(xs[1:], ys[1:])
    else:
        return []

# Return the common prefix of zero or more lists.
def commonPrefix(xss):
    return [] if not xss else list(foldr(commonPrefix2, xss[0], xss[1:]))

# Split a string into path components.
def splitPath(s):
    return [''.join(g) for k, g in groupby(s, lambda c: c != '/') if k]

# Return the common prefix of zero or more paths.
# Note that '/' by itself is not considered a path component,
# so "/" and "/foo" are treated as having nothing in common.
def commonDirPath(paths):
    return ''.join(commonPrefix(list(map(splitPath, paths))))

print(commonDirPath([
    "/home/user1/tmp/coverage/test",
    "/home/user1/tmp/covert/operator",
    "/home/user1/tmp/coven/members"
]))
```