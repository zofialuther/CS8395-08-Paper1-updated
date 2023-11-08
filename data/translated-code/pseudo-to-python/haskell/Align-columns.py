from itertools import takewhile

def main():
    dat = "Given$a$text$file$of$many$lines,$where$fields$within$a$line$\n" + \
          "are$delineated$by$a$single$'dollar'$character,$write$a$program\n" + \
          "that$aligns$each$column$of$fields$by$ensuring$that$words$in$each$\n" + \
          "column$are$separated$by$at$least$one$space.\n" + \
          "Further,$allow$for$each$word$in$a$column$to$be$either$left$\n" + \
          "justified,$right$justified,$or$center$justified$within$its$column.\n"

    def format(j, ls):
        def brkdwn(s):
            return takewhile(lambda x: x != '$', s), s[s.find('$')+1:]

        rows = [list(brkdwn(line)) for line in ls.split('\n')]
        colw = [max(len(word) for word in col) for col in zip(*rows)]
        
        def align(cw, w, j):
            dl = cw - len(w)
            l = dl // 2
            r = dl - l
            if j == 'c':
                return ' ' * l + w + ' ' * r
            elif j == 'r':
                return ' ' * dl + w
            elif j == 'l':
                return w + ' ' * dl

        return [' '.join(align(cw, w, j) for cw, w in zip(colw, row)) for row in rows]
    
    return format('c', dat)

print(main())