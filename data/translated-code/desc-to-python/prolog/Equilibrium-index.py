def equilibrium_index(lst, index):
    def sum_list(lst):
        if not lst:
            return 0
        else:
            return lst[0] + sum_list(lst[1:])
    
    def append(lst, part1, part2):
        if not lst:
            return part1, part2
        else:
            return append(lst[1:], part1 + [lst[0]], part2) if len(part1) <= len(part2) else append(lst[1:], part1, part2 + [lst[0]])
    
    part1, part2 = append(lst, [], [])
    sum1 = sum_list(part1)
    sum2 = sum_list(part2)
    
    if sum1 == sum2:
        return index
    else:
        return -1