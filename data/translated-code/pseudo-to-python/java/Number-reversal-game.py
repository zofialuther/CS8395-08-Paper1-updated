gameList = []
ReversalGame = None

def initialize():
    global gameList
    gameList = list(range(1, 10))
    shuffle(gameList)

def play():
    global gameList
    i = 0
    moveCount = 0
    while True:
        print(gameList)
        i = int(input("Enter an index to reverse from 2 to 9 or enter 99 to quit: "))
        if i == 99:
            break
        if i < 2 or i > 9:
            print("Invalid input")
        else:
            moveCount += 1
            reverse(i)
            if isSorted():
                print("Congratulations you solved this in " + str(moveCount) + " moves!")
                break

def reverse(position):
    global gameList
    gameList = gameList[:position] + gameList[position::-1]

def isSorted():
    global gameList
    for i in range(len(gameList) - 1):
        if gameList[i] > gameList[i + 1]:
            return False
    return True

def main():
    global ReversalGame
    try:
        initialize()
        play()
    except Exception as e:
        print("An error occurred:", e)
        traceback.print_exc()

if __name__ == "__main__":
    main()