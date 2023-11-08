```python
def dining_philosophers():
    D = create_window('Dining philosophers')
    S = create_window('Dining philosophers : statistics')
    set_window_size(D, 800, 800)

    E = create_ellipse(400, 400)
    set_ellipse_center(E, point(400, 400))
    display_window(D, E)

    F1 = create_forks()
    F2 = create_forks()
    F3 = create_forks()
    F4 = create_forks()
    F5 = create_forks()
    display_list(D, [F1,F2,F3,F4,F5])

    Waiter = create_waiter([F1, F2, F3, F4, F5])

    P1 = create_plate(0)
    P2 = create_plate(1)
    P3 = create_plate(2)
    P4 = create_plate(3)
    P5 = create_plate(4)

    Pt1 = create_point(0)
    Pt2 = create_point(1)
    Pt3 = create_point(2)
    Pt4 = create_point(3)
    Pt5 = create_point(4)

    Ph1 = create_philosopher('Aristotle', Waiter, P1, D, S, 0, Pt1, 'left')
    Ph2 = create_philosopher('Kant', Waiter, P2, D, S, 1, Pt2, 'left')
    Ph3 = create_philosopher('Spinoza', Waiter, P3, D, S, 2, Pt3, 'right')
    Ph4 = create_philosopher('Marx', Waiter, P4, D, S, 3, Pt4, 'right')
    Ph5 = create_philosopher('Russell', Waiter, P5, D, S, 4, Pt5, 'left')

    init_waiter_phi(Waiter, [Ph1, Ph2, Ph3, Ph4, Ph5])

    start_philosophers([Ph1, Ph2, Ph3, Ph4, Ph5])

    set_done_message(D, [Waiter, Ph1, Ph2, Ph3, Ph4, Ph5, S, D])

def create_plate(N):
    P = create_ellipse(80, 80)
    X = 400 + 140 * cos(N * pi / 2.5)
    Y = 400 + 140 * sin(N * pi / 2.5)
    set_ellipse_center(P, point(X, Y))

def create_point(N):
    X = 400 + 220 * cos(N * pi / 2.5)
    Y = 400 + 220 * sin(N * pi / 2.5) - 20
    return point(X, Y)

def create_waiter(F1, F2, F3, F4, F5):
    Waiter = create_waiter_object()
    set_waiter_forks(Waiter, F1, F2, F3, F4, F5)
    return Waiter

def create_philosopher(Name, Waiter, Plate, D, S, Index, Point, Side):
    Ph = create_philosopher_object(Name, Waiter, Plate, D, S, Index, Point, Side)
    return Ph

def init_waiter_phi(Waiter, Ph1, Ph2, Ph3, Ph4, Ph5):
    set_waiter_philosophers(Waiter, Ph1, Ph2, Ph3, Ph4, Ph5)

def start_philosophers(Ph1, Ph2, Ph3, Ph4, Ph5):
    start_philosopher(Ph1)
    start_philosopher(Ph2)
    start_philosopher(Ph3)
    start_philosopher(Ph4)
    start_philosopher(Ph5)

def set_done_message(D, Messages):
    send_done_message(D, Messages)
    open_window(D)
```