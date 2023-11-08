def theader(arr):
    return []

def theader(arr):
    return html(th(arr[0])).concat(theader(arr[1:]))

def trows(arr, n):
    if not arr:
        return []
    else:
        trRow = html(tr([td(n), trow(arr[0])]))
        n1 = n + 1
        return trRow.concat(trows(arr[1:], n1))

def trow(arr):
    if not arr:
        return []
    else:
        return html(td(arr[0])).concat(trow(arr[1:]))

def table():
    Header = ['X', 'Y', 'Z']
    Rows = [
        [7055, 5334, 5795],
        [2895, 3019, 7747],
        [140, 7607, 8144],
        [7090, 475, 4140]
    ]
    Out = phrase(html(table([tr(theader(Header)), trows(Rows, 1)])), Out, [])
    print_html(Out)