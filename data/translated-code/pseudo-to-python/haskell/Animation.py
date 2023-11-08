def runAnim():
    animationRunning = True
    while animationRunning:
        updateFrame()
        if frameCount >= maxFrameCount:
            animationRunning = False