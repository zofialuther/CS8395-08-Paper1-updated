def median(L, Z):
    Length = len(L) # Get the length of list L
    I = Length // 2 # Get the index for the median
    Rem = Length % 2 # Get the remainder when Length is divided by 2
    S = sorted(L) # Sort list L
    Mid = [0, 0]
    Mid[0] = I + Rem # Calculate the indices for the median
    Mid[1] = I + 1
    X = [0, 0]
    X[0] = S[Mid[0]] # Get the elements at the median indices
    X[1] = S[Mid[1]]
    Y = X[0] + X[1] # Calculate the sum of the median elements
    Z = Y / 2 # Calculate the median value and assign it to Z