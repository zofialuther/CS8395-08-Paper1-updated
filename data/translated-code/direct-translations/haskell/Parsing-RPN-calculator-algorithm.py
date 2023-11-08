from typing import TypeVar
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable

m = TypeVar('m')

class Logger(ABC):
    @abstractmethod
    def write(self, msg: str) -> m:
        pass

@dataclass
class IO(Logger):
    def write(self, msg: str) -> None:
        print(msg)

@dataclass
class Writer(Logger):
    def write(self, msg: str) -> None:
        print(msg)

def verbose2(f: Callable, x, y, logger: Logger) -> m:
    res = f(x, y)
    msg = f"{x} {y} ==> {res}\n"
    logger.write(msg)
    return res
```