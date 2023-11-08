def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks != 0:
        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
        print("Move disk " + str(ndisks) + " from peg " + str(startPeg) + " to peg " + str(endPeg))
        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)

hanoi(4)