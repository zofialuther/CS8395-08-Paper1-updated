def palindromic(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-1-i]:
            return False
    return True