from threading import Thread
import queue

def prime_decomp(number):
    # implementation of prime_decomp function
    pass

def threaded_decomp(number, id, results_queue):
    result = prime_decomp(number)
    results_queue.put((number, result))

def threaded_decomp_list(numbers):
    results_queue = queue.Queue()
    threads = []
    for number in numbers:
        thread = Thread(target=threaded_decomp, args=(number, results_queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results = []
    while not results_queue.empty():
        results.append(results_queue.get())

    return results

def pack_exit_out(result):
    return result[1]

def largest_min_factor(factors_list):
    largest = max(factors_list, key=lambda x: min(x[1]))
    return largest

def format_it(result):
    print(f"Number with largest minimal Factor is {result[0]}\nFactors are {result[1]}")

numbers = [100, 200, 300]
results = threaded_decomp_list(numbers)
largest_factor_result = largest_min_factor(results)
format_it(largest_factor_result)