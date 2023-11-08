def joins(str1, str2):
    return str1[-1] == str2[0]

def bind(func, lst):
    return [y for x in lst for y in func(x)]

def concatMap(func, lst):
    return [y for x in lst for y in func(x)]

def main():
    strings = ["hello", "orange", "eat", "table", "apple"]
    print(bind(lambda x: [x.upper()], strings))
    print(concatMap(lambda x: [x.upper()], strings))

main()