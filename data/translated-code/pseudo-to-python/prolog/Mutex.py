def synchronized_goal(G):
    acquire(my_mutex)
    G()
    release(my_mutex)