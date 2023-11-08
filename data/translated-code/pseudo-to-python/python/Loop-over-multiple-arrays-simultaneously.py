def print_zip(str1, str2, str3):
    zipped = list(zip(str1, str2, str3))
    joined = [''.join(x) for x in zipped]
    print('\n'.join(joined))