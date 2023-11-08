from time import sleep

try:
    print("Enter time to sleep in milliseconds:")
    delay = int(input())
    print("Sleeping...")
    sleep(delay / 1000)
    print("Awake!")
except ValueError:
    print("Invalid input")
except KeyboardInterrupt:
    print("Interrupted")