import time

def main():
    seconds = int(input("Enter the number of seconds: "))
    print("Sleeping...")
    time.sleep(seconds)
    print("Awake!")