def div(A, B, C, Ex):
    try:
        C = A / B
    except ZeroDivisionError as e:
        C = float('inf')