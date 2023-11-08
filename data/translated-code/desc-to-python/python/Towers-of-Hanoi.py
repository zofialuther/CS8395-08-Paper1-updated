def hanoi(n, start, end):
    if n == 1:
        print(f"Move disk 1 from peg {start} to peg {end}")
    else:
        other = 6 - start - end
        hanoi(n-1, start, other)
        print(f"Move disk {n} from peg {start} to peg {end}")
        hanoi(n-1, other, end)

hanoi(4, 1, 3)