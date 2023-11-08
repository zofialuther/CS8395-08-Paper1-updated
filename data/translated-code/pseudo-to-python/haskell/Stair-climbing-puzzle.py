def stepUp():
    def untilM(test, action):
        result = test()
        if result:
            return
        else:
            action()
            untilM(test, action)

    untilM(lambda: atEnd() and not clearAhead(), step)