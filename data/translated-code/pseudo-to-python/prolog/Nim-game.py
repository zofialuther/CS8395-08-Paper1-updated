def nim(N):
    if next_turn(12):
        return

def next_turn(N):
    PlayerGuess = int(input("How many dots would you like to take? "))
    while PlayerGuess not in [1, 2, 3]:
        PlayerGuess = int(input("How many dots would you like to take? "))
    
    N1 = N - PlayerGuess
    print("You take " + str(PlayerGuess) + " dots")
    print(str(N1) + " dots remaining.")
    
    CompGuess = 4 - PlayerGuess
    N2 = N1 - CompGuess
    print("Computer takes " + str(CompGuess) + " dots")
    print(str(N2) + " dots remaining.")
    
    if N2 == 0:
        print("Computer wins!")
    else:
        next_turn(N2)