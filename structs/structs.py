from queue import Queue as Fifo, LifoQueue as Lifo
from typing import Iterable


class Queue(Fifo):
    def __repr__(self) -> str:
        return str(list(self.queue))

    def __len__(self) -> int:
        return len(self.queue)

    def put_many(self, items: Iterable) -> None:
        for i in items:
            self.put(i)


class Stack(Lifo):
    def __repr__(self) -> str:
        return str(list(self.queue))

    def __len__(self) -> int:
        return len(self.queue)
    
    def put_many(self, items: Iterable) -> None:
        for i in items:
            self.put(i)
