from .CustomArray import DynamicArray
from .CustomLinkedList import DoublyLinkedList


class Stack:
    def __init__(self):
        self._items = DynamicArray()

    def __len__(self):
        return len(self._items)

    def is_empty(self):
        return len(self) == 0

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.delete_at(len(self) - 1)

    def peek(self):
        return self._items.get(len(self) - 1)


class Queue:
    def __init__(self):
        self._items = DoublyLinkedList()

    def __len__(self):
        return len(self._items)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        return self._items.delete_first()

    def peek(self):
        if self.is_empty():
            raise IndexError("Növbə boşdur.")
        return self._items.head.value

    def to_list(self):
        return self._items.to_list()


class Deque(Queue):
    """Hər iki ucundan əlavə etməyə və silməyə imkan verən növbə."""

    def add_front(self, value):
        self._items.prepend(value)

    def add_back(self, value):
        self.enqueue(value)

    def remove_front(self):
        return self.dequeue()

    def remove_back(self):
        return self._items.delete_last()

    def peek_front(self):
        return self.peek()

    def peek_back(self):
        if self.is_empty():
            raise IndexError("Növbə boşdur.")
        return self._items.tail.value
