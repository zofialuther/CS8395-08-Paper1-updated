import random

class Main:
    def main():
        scan = Scanner()
        random = Random()
        from_num = 1
        to_num = 100
        randomNumber = random.nextInt(to_num - from_num + 1) + from_num
        guessedNumber = 0
        print("The number is between", from_num, "and", to_num)
        
        while True:
            guessedNumber = scan.nextInt()
            if guessedNumber > randomNumber:
                print("Your guess is too high!")
            elif guessedNumber < randomNumber:
                print("Your guess is too low!")
            else:
                print("You got it!")
                break

if __name__ == "__main__":
    Main.main()