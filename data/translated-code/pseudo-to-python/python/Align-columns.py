from io import StringIO

textinfile = '''Given$a$text$file$of$many$lines,$where$fields$within$a$line$
are$delineated$by$a$single$'dollar'$character,$write$a$program
that$aligns$each$column$of$fields$by$ensuring$that$words$in$each$
column$are$separated$by$at$least$one$space.
Further,$allow$for$each$word$in$a$column$to$be$either$left$
justified,$right$justified,$or$center$justified$within$its$column.'''

j2justifier = dict(L=str.ljust, R=str.rjust, C=str.center)

def aligner(infile, justification='L'):
    assert justification in j2justifier, "justification can be L, R, or C; (Left, Right, or Centered)."
    justifier = j2justifier[justification]

    fieldsbyrow = []
    for line in infile:
        row = line.strip().split('$')
        fieldsbyrow.append(row)

    maxfields = 0
    for fields in fieldsbyrow:
        if len(fields) > maxfields:
            maxfields = len(fields)

    for fields in fieldsbyrow:
        for i in range(maxfields - len(fields)):
            fields.append('')

    fieldsbycolumn = []
    for i in range(maxfields):
        column = []
        for row in fieldsbyrow:
            column.append(row[i])
        fieldsbycolumn.append(column)

    colwidths = []
    for column in fieldsbycolumn:
        maxwidth = 0
        for field in column:
            if len(field) > maxwidth:
                maxwidth = len(field)
        colwidths.append(maxwidth)

    justifiedfields = []
    for i in range(len(fieldsbycolumn)):
        column = fieldsbycolumn[i]
        justifiedcolumn = []
        for j in range(len(column)):
            justifiedcolumn.append(justifier(column[j], colwidths[i]))
        justifiedfields.append(justifiedcolumn)

    justifiedrows = []
    for i in range(len(justifiedfields[0])):
        row = ''
        for j in range(len(justifiedfields)):
            row += justifiedfields[j][i] + ' '
        justifiedrows.append(row)

    return "\n".join(justifiedrows)

for align in 'Left Right Center'.split():
    infile = StringIO(textinfile)
    print("\n# %s Column-aligned output:" % align)
    print(aligner(infile, align[0]))