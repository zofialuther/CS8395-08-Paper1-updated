def f(x):
    foobar = 15  # using where clause
    return x + foobar

def f(x):
    let foobar = 15 in x + foobar  # using let...in expression

def f(x):
    do
        let foobar = 15
        x + foobar  # using do block with let statement