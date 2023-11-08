def show2d(arr):
    return '\n'.join([' '.join(['{:4}'.format(item) for item in row]) for row in arr])

def main(arrays):
    for arr in arrays:
        print(show2d(arr))