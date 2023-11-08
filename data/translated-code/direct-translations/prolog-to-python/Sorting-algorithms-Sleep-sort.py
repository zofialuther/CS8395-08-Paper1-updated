import threading
import time

def sleep_sort(L):
    thread_pool = threading.Thread(target=thread_pool_create, args=('rosetta', 1024, []))
    thread_pool.start()
    
    LID = [initsort(v) for v in L]
    _LStatus = [thread_join(id) for id in LID]
    
    thread_pool_destroy('rosetta')

def initsort(V):
    t = threading.Thread(target=thread_create_in_pool, args=('rosetta', (sleep(V), print(V)), None, []))
    t.start()
    return t

def thread_pool_create(name, size, args):
    # Function to create thread pool
    pass

def thread_create_in_pool(pool, target, id, args):
    # Function to create thread in pool
    pass

def thread_join(id):
    # Function to join thread
    pass

def thread_pool_destroy(name):
    # Function to destroy thread pool
    pass