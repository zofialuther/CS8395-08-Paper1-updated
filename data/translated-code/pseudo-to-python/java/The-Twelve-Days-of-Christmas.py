def main():
    days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    gifts = ["a partridge in a pear tree", "two turtle doves", "three French hens", "four calling birds", "five golden rings", "six geese a-laying", "seven swans a-swimming", "eight maids a-milking", "nine ladies dancing", "ten lords a-leaping", "eleven pipers piping", "twelve drummers drumming"]
    
    for i in range(len(days)):
        print("On the " + days[i] + " day of Christmas")
        print("My true love gave to me:")
        for j in range(i, -1, -1):
            if i == 11 and j < 2:
                print(gifts[j + 12])
            else:
                print(gifts[j])

main()