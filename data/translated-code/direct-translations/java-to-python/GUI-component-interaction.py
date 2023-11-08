from java.awt.event import KeyEvent, KeyListener

class FunctionalKeyListener(KeyListener):
    def keyPressed(self, event: KeyEvent):
        pass

    def keyTyped(self, event: KeyEvent):
        pass

    def keyReleased(self, event: KeyEvent):
        pass

    @FunctionalInterface
    class Pressed(FunctionalKeyListener):
        def keyPressed(self, event: KeyEvent):
            pass

    @FunctionalInterface
    class Typed(FunctionalKeyListener):
        def keyTyped(self, event: KeyEvent):
            pass

    @FunctionalInterface
    class Released(FunctionalKeyListener):
        def keyReleased(self, event: KeyEvent):
            pass