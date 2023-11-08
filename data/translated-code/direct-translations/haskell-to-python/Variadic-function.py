from typing import TypeVar, IO
from typing_extensions import Protocol

A = TypeVar('A')

class PrintAllType(Protocol):
    def process(self, args: IO[A]) -> None:
        ...

    def __getitem__(self, args: int) -> A:
        ...

    def __setitem__(self, args: int, value: A) -> None:
        ...

    def __delitem__(self, args: int) -> None:
        ...

    def __len__(self) -> int:
        ...

    def __iter__(self) -> Iterator[A]:
        ...

    def __next__(self) -> A:
        ...

    def __contains__(self, item: object) -> bool:
        ...

    def __reversed__(self) -> Iterator[A]:
        ...

    def __add__(self, other: IO[A]) -> IO[A]:
        ...

    def __sub__(self, other: IO[A]) -> IO[A]:
        ...

    def __mul__(self, other: IO[A]) -> IO[A]:
        ...

    def __truediv__(self, other: IO[A]) -> IO[A]:
        ...

    def __floordiv__(self, other: IO[A]) -> IO[A]:
        ...

    def __mod__(self, other: IO[A]) -> IO[A]:
        ...

    def __divmod__(self, other: IO[A]) -> Tuple[IO[A], IO[A]]:
        ...

    def __pow__(self, other: IO[A], modulo: Optional[IO[A]] = ...) -> IO[A]:
        ...

    def __lshift__(self, other: IO[A]) -> IO[A]:
        ...

    def __rshift__(self, other: IO[A]) -> IO[A]:
        ...

    def __and__(self, other: IO[A]) -> IO[A]:
        ...

    def __xor__(self, other: IO[A]) -> IO[A]:
        ...

    def __or__(self, other: IO[A]) -> IO[A]:
        ...

    def __neg__(self) -> IO[A]:
        ...

    def __pos__(self) -> IO[A]:
        ...

    def __abs__(self) -> IO[A]:
        ...

    def __invert__(self) -> IO[A]:
        ...

    def __complex__(self) -> complex:
        ...

    def __int__(self) -> int:
        ...

    def __float__(self) -> float:
        ...

    def __round__(self, n: Optional[int] = ...) -> IO[A]:
        ...

    def __index__(self) -> int:
        ...

    def __trunc__(self) -> IO[A]:
        ...

    def __floor__(self) -> IO[A]:
        ...

    def __ceil__(self) -> IO[A]:
        ...

    def __enter__(self) -> IO[A]:
        ...

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]) -> Optional[bool]:
        ...

    def __await__(self) -> IO[A]:
        ...

    def __aiter__(self) -> AsyncIterator[A]:
        ...

    def __anext__(self) -> A:
        ...

    def __aenter__(self) -> IO[A]:
        ...

    def __aexit__(self, exc_type: Optional[Type[BaseException]], exc: Optional[BaseException], tb: Optional[TracebackType]) -> Awaitable[None]:
        ...

    def __aiter__(self) -> AsyncIterator[A]:
        ...

    def __anext__(self) -> A:
        ...

    def __contains__(self, item: object) -> bool:
        ...

    def __await__(self) -> IO[A]:
        ...

    def __aiter__(self) -> AsyncIterator[A]:
        ...

    def __anext__(self) -> A:
        ...

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]) -> Optional[bool]:
        ...

    def __await__(self) -> IO[A]:
        ...

    def __aiter__(self) -> AsyncIterator[A]:
        ...

    def __anext__(self) -> A:
        ...

    def __enter__(self) -> IO[A]:
        ...

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]) -> Optional[bool]:
        ...

    def __contains__(self, item: object) -> bool:
        ...

    def __await__(self) -> IO[A]:
        ...

    def __aiter__(self) -> AsyncIterator[A]:
        ...

    def __anext__(self) -> A:
        ...

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]) -> Optional[bool]:
        ...

    def __await__(self) -> IO[A]:
        ...

    def __aiter__(self) -> AsyncIterator[A]:
        ...

    def __anext__(self) -> A:
        ...

    def __contains__(self, item: object) -> bool:
        ...

    def __await__(self) -> IO[A]:
        ...

    def __aiter__(self) -> AsyncIterator[A]:
        ...

    def __anext__(self) -> A:
        ...

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]) -> Optional[bool]:
        ...

    def __await__(self) -> IO[A]:
        ...

    def __aiter__(self) -> AsyncIterator[A]:
        ...

    def __anext__(self) -> A:
        ...

    def __contains__(self, item: object) -> bool:
        ...

    def __await__(self) -> IO[A]:
        ...

    def __aiter__(self) -> AsyncIterator[A]:
        ...

    def __anext__(self) -> A:
        ...

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]) -> Optional[bool]:
        ...


def process(args: IO[A], instance: PrintAllType) -> None:
    mapM_ = instance.__contains__
    mapM_(print, args)