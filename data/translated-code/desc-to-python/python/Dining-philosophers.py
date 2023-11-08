import multiprocessing
import random
import time

def philosopher(name, left, right):
    # Simulate thinking and dining using random schedules
    while True:
        print(f'Philosopher {name} is thinking')
        time.sleep(random.uniform(0, 1))
        print(f'Philosopher {name} is hungry')
        with left, right:
            print(f'Philosopher {name} is eating')
            time.sleep(random.uniform(0, 1))

def main():
    # Set up the philosophers and chopsticks
    chopsticks = [multiprocessing.Lock() for _ in range(5)]
    philosophers = [multiprocessing.Process(target=philosopher, args=(i, chopsticks[i], chopsticks[(i + 1) % 5])) for i in range(5)]

    # Start the philosopher processes
    for p in philosophers:
        p.start()

    # Run the simulation for a specified duration
    time.sleep(10)

    # Terminate the philosopher processes
    for p in philosophers:
        p.terminate()

if __name__ == "__main__":
    main()