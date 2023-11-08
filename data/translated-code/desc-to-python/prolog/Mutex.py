from threading import Lock

def synchronized_goal(G):
    my_mutex = Lock()
    with my_mutex:
        # execute the goal G
        G()