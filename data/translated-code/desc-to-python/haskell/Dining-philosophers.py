```python
# Philosopher module
import threading
import time

class Fork:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()

def create_forks(num_forks):
    forks = [Fork(str(i)) for i in range(num_forks)]
    return forks

def take_forks(left_fork, right_fork):
    while True:
        if left_fork.lock.acquire(blocking=False):
            if right_fork.lock.acquire(blocking=False):
                return
            else:
                left_fork.lock.release()

def release_forks(left_fork, right_fork):
    left_fork.lock.release()
    right_fork.lock.release()

def philosopher(name, left_fork, right_fork):
    while True:
        print(f'{name} is thinking')
        time.sleep(1)

        print(f'{name} is hungry')
        take_forks(left_fork, right_fork)

        print(f'{name} is eating')
        time.sleep(1)

        print(f'{name} has finished eating')
        release_forks(left_fork, right_fork)

def main():
    num_forks = 5
    forks = create_forks(num_forks)
    philosophers = ['Philo' + str(i) for i in range(num_forks)]
    threads = []

    for i in range(num_forks):
        t = threading.Thread(target=philosopher, args=(philosophers[i], forks[i], forks[(i+1) % num_forks]))
        threads.append(t)
        t.start()

    input("Press enter to quit")

if __name__ == "__main__":
    main()
```