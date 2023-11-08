import numpy as np
from random import shuffle

# Function to generate random text
def gen(n):
    txt = list('[]' * n)  # Create a list of '[]' repeated n times
    shuffle(txt)  # Shuffle the list
    return ''.join(txt)  # Convert the list to a string and return

# Create an array m using numpy with mapping for '[' and ']'
m = np.array([{'[': 1, ']': -1}.get(chr(c), 0) for c in range(128)])

# Function to check if the input text is balanced
def balanced(txt):
    a = np.array(txt, 'c').view(np.uint8)  # Convert the input text to a numpy array of type 'c' and then to uint8
    return np.all(m[a].cumsum() >= 0)  # Check if the cumulative sum of m[a] is greater than or equal to 0 for all elements

# Generate random text and check if it is balanced
for txt in (gen(N) for N in range(10)):
    print ("%-22r is%s balanced" % (txt, '' if balanced(txt) else ' not'))  # Print the text and whether it is balanced or not