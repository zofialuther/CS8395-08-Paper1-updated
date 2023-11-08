def drawTree2(blnCompact):
    def go(blnPruned, tree):
        def measured(x):
            s = ' ' + str(x) + ' '
            return (len(s), s)
        
        def lmrFromStrings(xs):
            i = len(xs) // 2
            ls, rs = xs[0:i], xs[i:]
            return ls, rs[0], rs[1:]
        
        def stringsFromLMR(lmr):
            ls, m, rs = lmr
            return ls + [m] + rs
        
        def fghOverLMR(f, g, h):
            def go(lmr):
                ls, m, rs = lmr
                return ([f(x) for x in ls], g(m), [h(x) for x in rs])
            return go
        
        def leftPad(n):
            return lambda s: (' ' * n) + s
        
        def treeFix(l, m, r):
            def cfix(x):
                return lambda xs: x + xs
            return compose(stringsFromLMR)(fghOverLMR(cfix(l), cfix(m), cfix(r)))
        
        def lmrBuild(w, f):
            def go(wsTree):
                nChars, x = wsTree['root']
                _x = ('─' * (w - nChars)) + x
                xs = wsTree['nest']
                lng = len(xs)
                
                if lng == 0:
                    return ([], _x, [])
                elif lng == 1:
                    return fghOverLMR(rightAligned, lineLinked, rightAligned)(f(xs[0]))
                else:
                    lmrs = [f(x) for x in xs]
                    return fghOverLMR(rightAligned, linked, rightAligned)(lmrFromStrings(intercalate([] if blnCompact else ['│'])([treeFix(' ', '┌', '│')(lmrs[0])] + [treeFix('│', '├', '│')(x) for x in lmrs[1:-1]] + [treeFix('│', '└', ' ')(lmrs[-1])])))
            return lambda wsTree: go(wsTree)
        
        measuredTree = fmapTree(measured)(tree)
        levelWidths = reduce(lambda a, xs: a + [max(x[0] for x in xs)], levels(measuredTree), [])
        treeLines = stringsFromLMR(foldr(lmrBuild)(None)(levelWidths)(measuredTree))
        return [s for s in treeLines if any(c not in '│ ' for c in s)] if (not blnCompact and blnPruned) else treeLines
    return lambda blnPruned: (lambda tree: '\n'.join(go(blnPruned, tree)))