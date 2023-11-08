def stepUp():
    untilM(step(), stepUp())

def untilM(test, action):
    result = test
    if result:
        return
    else:
        action
        untilM(test, action)