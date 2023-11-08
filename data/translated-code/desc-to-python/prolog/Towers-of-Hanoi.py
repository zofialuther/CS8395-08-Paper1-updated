def hanoi(N):
    def move(n, source, target, auxiliary):
        if n > 0:
            move(n-1, source, auxiliary, target)
            inform(f"Move disk {n} from {source} to {target}")
            move(n-1, auxiliary, target, source)
    
    def inform(message):
        print(message)
    
    move(N, 'A', 'C', 'B')