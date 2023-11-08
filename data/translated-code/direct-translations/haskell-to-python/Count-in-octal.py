import numpy as np

def main():
    for i in range(1, np.iinfo(np.int32).max):
        print(oct(i))

main()