def main():
    print("Please enter the range:")
    from_input = input("From: ")
    to_input = input("To: ")
    if (from_input, to_input):
        from_value = int(from_input)
        to_value = int(to_input)
        if from_value < to_value:
            loop(from_value, to_value)
    else:
        print("Invalid input.")
        main()

def loop(from_value, to_value):
    guess = (to_value + from_value) // 2
    answer = input(f"Is it {guess}? ((l)ower, (c)orrect, (h)igher)")
    if answer == "c":
        print("Awesome!")
    elif answer == "l":
        loop(from_value, guess)
    elif answer == "h":
        loop(guess, to_value)
    else:
        print("Invalid answer.")
        loop(from_value, to_value)

main()