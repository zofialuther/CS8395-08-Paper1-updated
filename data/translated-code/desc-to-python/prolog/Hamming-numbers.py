def hamming_numbers(N=20):
    hamming_list = [1]
    i, j, k = 0, 0, 0
    
    while len(hamming_list) < N:
        next_hamming = min(hamming_list[i]*2, hamming_list[j]*3, hamming_list[k]*5)
        hamming_list.append(next_hamming)
        
        if next_hamming == hamming_list[i]*2:
            i += 1
        if next_hamming == hamming_list[j]*3:
            j += 1
        if next_hamming == hamming_list[k]*5:
            k += 1
    
    return hamming_list