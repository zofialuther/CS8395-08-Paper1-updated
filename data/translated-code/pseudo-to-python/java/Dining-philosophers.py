```python
import threading
import random
import time

ON_TABLE = -1
philosopher_count = 5
run_seconds = 15

class PhilosopherState:
    Get = 0
    Eat = 1
    Pon = 2

class Fork:
    instances = 0

    def __init__(self):
        self.id = Fork.instances
        Fork.instances += 1
        self.holder = ON_TABLE

class Philosopher(threading.Thread):
    max_wait_ms = 100
    token = 0
    instances = 0

    def __init__(self):
        super(Philosopher, self).__init__()
        self.id = Philosopher.instances
        Philosopher.instances += 1
        self.state = PhilosopherState.Get
        self.left = forks[self.id]
        self.right = forks[(self.id + 1) % philosopher_count]
        self.times_eaten = 0
        self.end = False

    def sleep(self):
        time.sleep(random.randint(0, self.max_wait_ms)/1000)

    def wait_for_fork(self, fork):
        while True:
            if fork.holder == ON_TABLE:
                fork.holder = self.id
                return
            else:
                self.sleep()

    def run(self):
        while not self.end:
            if self.state == PhilosopherState.Pon:
                self.state = PhilosopherState.Get
            else:
                if Philosopher.token == self.id:
                    self.wait_for_fork(self.left)
                    self.wait_for_fork(self.right)
                    Philosopher.token = (self.id + 2) % philosopher_count
                    self.state = PhilosopherState.Eat
                    self.times_eaten += 1
                    self.sleep()
                    self.left.holder = ON_TABLE
                    self.right.holder = ON_TABLE
                    self.state = PhilosopherState.Pon
                    self.sleep()
                else:
                    self.sleep()

forks = [Fork() for _ in range(philosopher_count)]
philosophers = [Philosopher() for _ in range(philosopher_count)]

for p in philosophers:
    p.start()

end_time = time.time() + run_seconds

while time.time() < end_time:
    state_output = "|"
    for p in philosophers:
        state_output += str(p.state) + "|"
    state_output += "     |"
    for f in forks:
        holder = f.holder
        state_output += "   " if holder == ON_TABLE else "P{:02d}".format(holder)
        state_output += "|"
    print(state_output)
    time.sleep(1)

for p in philosophers:
    p.end = True

for p in philosophers:
    print(f"P{p.id:02d}: ate {p.times_eaten} times, {p.times_eaten // run_seconds} / sec")
```