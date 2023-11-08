def main():
    tokens = 12
    while tokens > 0:
        user_choice = int(input("Enter 1, 2, or 3: "))
        if user_choice < 1 or user_choice > 3:
            print("Invalid input. Please enter 1, 2, or 3.")
            continue
        tokens -= user_choice
        if tokens <= 0:
            print("You win!")
            break
        computer_choice = 4 - user_choice
        print(f"The computer takes {computer_choice} tokens.")
        tokens -= computer_choice
        if tokens <= 0:
            print("Computer wins!")
            break

main()