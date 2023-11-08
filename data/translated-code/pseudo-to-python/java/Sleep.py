from time import sleep

class Sleep:
    def main(self):
        try:
            print("Enter time to sleep in milliseconds:")
            delay = int(input())
            print("Sleeping...")
            sleep(delay / 1000)
            print("Awake!")
        except (ValueError, KeyboardInterrupt):
            print("Invalid input or interrupted")
        except Exception as e:
            print("An error occurred:", e)