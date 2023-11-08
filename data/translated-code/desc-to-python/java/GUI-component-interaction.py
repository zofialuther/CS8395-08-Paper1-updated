```python
from abc import ABC, abstractmethod
from java.awt.event import KeyListener

class FunctionalKeyListener(KeyListener, ABC):
    
    @abstractmethod
    def keyPressed(self, e):
        pass
    
    @abstractmethod
    def keyTyped(self, e):
        pass
    
    @abstractmethod
    def keyReleased(self, e):
        pass

class Pressed(FunctionalKeyListener, ABC):
    
    @abstractmethod
    def handlePressed(self, e):
        pass

class Typed(FunctionalKeyListener, ABC):
    
    @abstractmethod
    def handleTyped(self, e):
        pass

class Released(FunctionalKeyListener, ABC):
    
    @abstractmethod
    def handleReleased(self, e):
        pass
```