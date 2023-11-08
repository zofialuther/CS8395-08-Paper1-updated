from constraint import *

def compound_time(N):
    R = times(N)
    print(N, ":")
    write_times(R)

def write_times(T):
    if T:
        print(T[0][1], T[0][0])
        write_times(T[1:])
    if len(T) == 1:
        print(T[0][1], T[0][0])

def times(N, TTs=None, R=None):
    if TTs is None:
        TTs = ['weeks', 'days', 'hours', 'minutes', 'seconds']
    times(TTs, N, R)

def times(T, N, R):
    if not T:
        R = []
    if T:
        Tt, Div = T[0]
        Val = N // Div
        if Val < 1:
            times(T[1:], N, R)
        if Val >= 1:
            Rem = N % Div
            times(T[1:], Rem, [[Tt,Val]] + R)

def time_type():
    weeks = 60 * 60 * 24 * 7
    days = 60 * 60 * 24
    hours = 60 * 60
    minutes = 60
    seconds = 1