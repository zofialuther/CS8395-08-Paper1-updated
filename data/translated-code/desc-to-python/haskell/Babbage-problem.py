def findBabbageNumber():
    num = 1
    while True:
        if str(num*num).endswith("269696"):
            return num
        num += 1

def main():
    babbage_number = findBabbageNumber()
    babbage_square = babbage_number * babbage_number
    print(f"The Babbage number is {babbage_number} and its square is {babbage_square}.")
    print("This is the square of the original number.")

main()