import collections
import re
import string
import sys

# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python program_name.py input_file.txt integer_value")
    sys.exit(1)

input_file = sys.argv[1]
integer_value = int(sys.argv[2])

# Your code to read the file, count word occurrences, and print the most common words with their frequencies based on the integer provided.