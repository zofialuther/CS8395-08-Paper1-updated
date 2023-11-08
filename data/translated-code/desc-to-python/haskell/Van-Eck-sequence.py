def van_eck_sequence(n):
    sequence = [0]
    last_seen = {0: 1}
    
    for i in range(1, n):
        if sequence[i-1] in last_seen and last_seen[sequence[i-1]] > 1:
            sequence.append(i - 1 - last_seen[sequence[i-1]])
            if sequence[i-1 - last_seen[sequence[i-1]]] in last_seen:
                last_seen[sequence[i-1 - last_seen[sequence[i-1]]]] = i
            else:
                last_seen[sequence[i-1 - last_seen[sequence[i-1]]]] = i
        else:
            sequence.append(0)
            last_seen[0] = i
    
    return sequence

print(van_eck_sequence(10))