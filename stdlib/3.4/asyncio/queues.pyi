from typing import TypeVar, Generic

__all__ = ...  # type: str

from asyncio.events import AbstractEventLoop
from .coroutines import coroutine
from .futures import Future


class QueueEmpty(Exception): ...
class QueueFull(Exception): ...

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self, maxsize: int = ..., *, loop: AbstractEventLoop = ...) -> None: ...
    def _init(self, maxsize: int) -> None: ...
    def _get(self) -> T: ...
    def _put(self, item: T) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def _format(self) -> str: ...
    def _consume_done_getters(self) -> None: ...
    def _consume_done_putters(self) -> None: ...
    def qsize(self) -> int: ...
    @property
    def maxsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    @coroutine
    def put(self, item: T) -> Future[None]: ...
    def put_nowait(self, item: T) -> None: ...
    @coroutine
    def get(self) -> Future[T]: ...
    def get_nowait(self) -> T: ...


class PriorityQueue(Queue): ...


class LifoQueue(Queue): ...


class JoinableQueue(Queue):
    def task_done(self) -> None: ...
    @coroutine
    def join(self) -> None: ...
