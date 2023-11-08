def forLoop(Hi, Lo, Step):
    if (Step < 0 and Lo <= Hi):
        for i in range(Hi, Lo-1, Step):
            # do something
    elif (Step < 0):
        V = Hi + Step
        if (Lo <= V):
            forLoop(V, Lo, Step)