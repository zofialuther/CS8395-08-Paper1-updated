from concurrent import futures

def main():
  def process1():
    print("Enjoy")
  def process2():
    print("Rosetta")
  def process3():
    print("Code")

  processes = [process1, process2, process3]

  with futures.ThreadPoolExecutor() as executor:
    executor.map(executor.submit, processes)