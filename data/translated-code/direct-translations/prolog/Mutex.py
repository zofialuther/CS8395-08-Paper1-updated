from threading import Lock

my_mutex = Lock()

def synchronized_goal(G):
    with my_mutex:
        G()