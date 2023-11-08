def partitions(number, summands):
    # Function to calculate partitions
    def calculate_partitions(n, m):
        if n == 0 and m == 0:
            return [[]]
        elif n < 0 or m == 0:
            return []
        else:
            partitions_list = []
            for i in range(min(n, m), 0, -1):
                for p in calculate_partitions(n - i, i):
                    partitions_list.append([i] + p)
            return partitions_list

    return calculate_partitions(number, summands)

def test_partitions():
    print(partitions(5, 3))
    print(partitions(7, 2))
    print(partitions(10, 4))

def justifyLeft(string, width):
    return string.ljust(width)