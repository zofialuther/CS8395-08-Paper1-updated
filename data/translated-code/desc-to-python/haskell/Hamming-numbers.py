def hammings(n):
    hamming_list = [1]
    i2, i3, i5 = 0, 0, 0
    next_2, next_3, next_5 = 2, 3, 5
    
    for _ in range(1, n):
        next_hamming = min(next_2, next_3, next_5)
        hamming_list.append(next_hamming)
        
        if next_hamming == next_2:
            i2 += 1
            next_2 = hamming_list[i2] * 2
        if next_hamming == next_3:
            i3 += 1
            next_3 = hamming_list[i3] * 3
        if next_hamming == next_5:
            i5 += 1
            next_5 = hamming_list[i5] * 5
    
    return hamming_list

def main():
    hamming_numbers = hammings(1000000)
    print(hamming_numbers[:20])
    print(hamming_numbers[1689])
    print(hamming_numbers[999999])

main()