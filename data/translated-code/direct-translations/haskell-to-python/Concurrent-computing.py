import threading

def process1():
    print("Enjoy")

def process2():
    print("Rosetta")

def process3():
    print("Code")

threads = [threading.Thread(target=process1), threading.Thread(target=process2), threading.Thread(target=process3)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()