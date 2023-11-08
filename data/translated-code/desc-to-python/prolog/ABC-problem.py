def abc_problem(words, L):
    def check_word(word, L):
        if len(word) <= 1:
            return True
        else:
            pair = word[0:2]
            if pair in L:
                return check_word(word[2:], L)
            else:
                return False

    for word in words:
        if check_word(word, L):
            print("OK")
        else:
            print("KO")