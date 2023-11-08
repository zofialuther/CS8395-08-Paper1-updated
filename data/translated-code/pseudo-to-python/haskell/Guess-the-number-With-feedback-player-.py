def main():
    print("Please enter the range:")
    print("From: ")
    from_num = int(input())
    print("To: ")
    to = int(input())
    if (from_num.isdigit()) and (to.isdigit()) and (from_num < to):
        loop(from_num, to)
    else:
        print("Invalid input.")
        main()

def loop(from_num, to):
    guess = (to + from_num) / 2
    print("Is it " + str(guess) + "? ((l)ower, (c)orrect, (h)igher)")
    answer = input()
    if answer == "c":
        print("Awesome!")
    elif answer == "l":
        loop(from_num, guess)
    elif answer == "h":
        loop(guess, to)
    else:
        print("Invalid answer.")
        loop(from_num, to)