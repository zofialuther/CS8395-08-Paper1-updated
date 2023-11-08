def test():
    InFile = 'test.csv'
    OutFile = 'test.out.csv'
    augment(InFile, OutFile)

def augment(InFile, OutFile):
    with open(OutFile, 'w') as OutStream:
        # Repeat the following steps:
        # Read a row from InFile and assign it to Row, with Line as the line number
        # If reading the row was successful, do the following:
        # Call addrow with Row as the Term and assign the result to Out
        # Write Out to the OutStream as a CSV row
        # If reading the row was not successful, close the OutStream
    OutStream.close()

def addrow(Term, NewTerm):
    # Extract the functor and the list of items from Term
    # Get the first item from the list and assign it to X
    # If X is an integer, calculate the sum of the list and assign it to Sum; otherwise, assign 'SUM' to Sum
    # Append Sum to the end of the list and assign it to NewList
    # Create a new term with the same functor as Term and NewList as the list of items, and assign it to NewTerm