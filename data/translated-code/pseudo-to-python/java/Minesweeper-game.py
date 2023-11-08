def intErrorTrap(x, y):
    max = 0
    min = 0
    input = 0
    loopEnd = False

    if x < y:
        min = x
        max = y
    else:
        min = y
        max = x

    while loopEnd == False:
        print("Please enter an integer between " + str(min) + " to " + str(max) + ".")
        userInput = input()

        try:
            input = int(userInput)

            if input > max:
                loopEnd = False
                print("Input is invalid.")
                return -1
            elif input < min:
                loopEnd = False
                print("Input is invalid.")
                return -1
            else:
                loopEnd = True
                print(str(input) + " is a valid input.")
                return input
        except Exception as e:
            loopEnd = False
            userInput = None
            print("Input is invalid.")
            return 0


def main(args):
    print("Enter width.")
    x = intErrorTrap(0, 60)
    
    print("Enter height.")
    y = intErrorTrap(0, 30)
    
    print("Enter difficulty.")
    d = intErrorTrap(0, 100)

    # create new Minesweeper(x, y, d) - This line is not part of the provided pseudocode so it is not included in the Python code.