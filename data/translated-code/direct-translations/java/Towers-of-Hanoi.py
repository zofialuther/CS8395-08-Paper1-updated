# Python code to move disks from one pole to another using the Tower of Hanoi algorithm

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print(f"Move disk from pole {source} to pole {destination}")
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print(f"Move disk from pole {source} to pole {destination}")
    TowerOfHanoi(n-1, auxiliary, destination, source)

# Driver code
n = 3
TowerOfHanoi(n, '1', '2', '3')