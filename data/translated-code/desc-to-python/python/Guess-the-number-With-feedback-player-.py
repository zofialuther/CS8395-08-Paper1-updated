import bisect

class GuessNumberFakeList:
    def __init__(self, number):
        self.number = number

    def guess_number(self):
        print("Guess a number between 0 and 100")
        print("I will ask you if your number is less than or equal to a specific value")

        fake_list = [i for i in range(101)]
        guess = 0
        
        while guess != self.number:
            index = int(input(f"Is your number less than or equal to {fake_list[len(fake_list)//2]}? (0/1): "))
            if index == 1:
                fake_list = fake_list[:len(fake_list)//2 + 1]
            else:
                fake_list = fake_list[len(fake_list)//2:]
            
            guess = fake_list[len(fake_list)//2]

        print(f"Your number is {guess}")

# Example usage
game = GuessNumberFakeList(57)
game.guess_number()