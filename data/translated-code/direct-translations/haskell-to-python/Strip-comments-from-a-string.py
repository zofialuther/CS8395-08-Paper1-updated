ms = ";#"

main = getContents() >> \
       mapM_(lambda line: print(''.join(takewhile(lambda c: c not in ms, line))),  lines())