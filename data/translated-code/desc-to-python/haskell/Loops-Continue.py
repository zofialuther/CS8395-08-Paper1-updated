from Control.Monad import forM_

def out(num):
    if num % 5 == 0:
        print(num)
    else:
        print(num, end=", ")

forM_([1,2,3,4,5,6,7,8,9,10], out)