```python
import threading
import random
import time

ON_TABLE = -1
instances = 0
maxWaitMs = 100
token = 0
philosopherCount = 5
runSeconds = 15
forks = []
philosophers = []

class PhilosopherState:
    Get = 1
    Eat = 2
    Pon = 3

class Fork:
    def __init__(self):
        global instances
        self.id = instances
        instances += 1
        self.holder = ON_TABLE

class Philosopher(threading.Thread):
    def __init__(self):
        global instances
        threading.Thread.__init__(self)
        self.id = instances
        instances += 1
        self.state = PhilosopherState.Get
        self.left = forks[self.id]
        self.right = forks[(self.id+1)%philosopherCount]
        self.timesEaten = 0

    def sleep(self):
        time.sleep(random.randint(0, maxWaitMs) / 1000)

    def waitForFork(self, fork):
        while True:
            if fork.holder == ON_TABLE:
                fork.holder = self.id
                return
            else:
                self.sleep()

    def run(self):
        global token
        while True:
            if self.state == PhilosopherState.Pon:
                self.state = PhilosopherState.Get
            else:
                if token == self.id:
                    self.waitForFork(self.left)
                    self.waitForFork(self.right)
                    token = (self.id + 2) % philosopherCount
                    self.state = PhilosopherState.Eat
                    self.timesEaten += 1
                    self.sleep()
                    self.left.holder = ON_TABLE
                    self.right.holder = ON_TABLE
                    self.state = PhilosopherState.Pon
                    self.sleep()
                else:
                    self.sleep()

for i in range(philosopherCount):
    forks.append(Fork())

for i in range(philosopherCount):
    philosophers.append(Philosopher())

for p in philosophers:
    p.start()

end_time = time.time() + runSeconds

while time.time() < end_time:
    status = "|"
    for p in philosophers:
        status += p.state.name + "|"
    status += "     |"
    for f in forks:
        holder = f.holder
        status += "   " if holder == -1 else "P{:02d}".format(holder) + "|"
    print(status)
    time.sleep(1)

for p in philosophers:
    p.join()
    print("P{:02d}: ate {:,} times, {:,}/sec".format(p.id, p.timesEaten, int(p.timesEaten/runSeconds)))
```