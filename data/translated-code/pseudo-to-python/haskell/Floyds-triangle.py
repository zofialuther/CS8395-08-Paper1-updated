floyds = [[1]]

def floyd(lst):
    if len(lst) < 2:
        return [1]
    else:
        n = len(lst) + 1
        return list(range((n * (n - 1)) // 2, (n * (n + 1)) // 2))

def main():
    floyds = [floyd([1])]
    for i in range(5):
        print(floyds[0][i])
        
    print()

    for i in range(14):
        print(floyds[0][i])