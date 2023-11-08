```python
from abc import ABC, abstractmethod
from typing import Type
import keyboard

class FunctionalKeyListener(ABC):
    @abstractmethod
    def keyPressed(self, event):
        pass

    @abstractmethod
    def keyTyped(self, event):
        pass

    @abstractmethod
    def keyReleased(self, event):
        pass

class Pressed(FunctionalKeyListener):
    @abstractmethod
    def keyPressed(self, event):
        pass

class Typed(FunctionalKeyListener):
    @abstractmethod
    def keyTyped(self, event):
        pass

class Released(FunctionalKeyListener):
    @abstractmethod
    def keyReleased(self, event):
        pass
```