areDigits = all(str.isdigit)
isOctDigit = all(lambda x: x in '01234567')
isHexDigit = all(lambda x: x.isdigit() or x in 'ABCDEFabcdef')