try:
    a = someValue
    assert a == 42
    return somethingElse
except AssertionError:
    raise Exception("AssertionFailed")