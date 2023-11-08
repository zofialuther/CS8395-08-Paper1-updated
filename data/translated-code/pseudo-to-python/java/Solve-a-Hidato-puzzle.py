class Hidato:
    board = []
    given = []
    start = []

    def main(self):
        input = ["input values"] # Replace with actual input values
        self.setup(input)
        self.printBoard()
        print("Found:")
        self.solve(start[0], start[1], 1, 0)
        self.printBoard()

    def setup(self, input):
        # Populate puzzle array
        # Get number of columns and rows
        # Create new ArrayList
        # Initialize board array
        # Populate board array
        # Sort list and populate given array

    def solve(self, r, c, n, next):
        # Check if n is greater than last value in given array
        # Check if value in board array at position r and c is not 0 and not equal to n
        # Check if value in board array at position r and c is 0 and next value in given array is equal to n
        # Set variable back and check if back is equal to n
        # Set value in board array at position r and c to n
        # Loop through adjacent cells and recursively call solve method
        # Set value in board array at position r and c back to its original value and return false

    def printBoard(self):
        # Loop through board array and print values with appropriate formatting
        pass