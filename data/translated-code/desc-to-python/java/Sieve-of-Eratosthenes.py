class InfiniteSieve:
    def __init__(self):
        self.queue = []
        self.num = 2
    
    def generate_primes(self):
        while True:
            if not any(self.num % p == 0 for p in self.queue):
                yield self.num
                self.queue.append(self.num)
            else:
                for p in self.queue:
                    if self.num % p == 0:
                        self.queue.remove(p)
                        break
            self.num += 1

if __name__ == "__main__":
    sieve = InfiniteSieve()
    prime_generator = sieve.generate_primes()
    for _ in range(25):
        print(next(prime_generator))