class SNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def _nodes(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def prepend(self, value):
        self.head = SNode(value, self.head)
        self.size += 1

    def append(self, value):
        if self.head is None:
            self.prepend(value)
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = SNode(value)
        self.size += 1

    def _remove(self, previous, node):
        if previous is None:
            self.head = node.next
        else:
            previous.next = node.next
        self.size -= 1
        return node.value

    def delete_first(self):
        if self.head is None:
            raise IndexError("Siyahı boşdur.")
        return self._remove(None, self.head)

    def delete_last(self):
        if self.head is None:
            raise IndexError("Siyahı boşdur.")
        previous, node = None, self.head
        while node.next is not None:
            previous, node = node, node.next
        return self._remove(previous, node)

    def delete_value(self, value):
        previous = None
        for node in self._nodes():
            if node.value == value:
                self._remove(previous, node)
                return True
            previous = node
        return False

    def search(self, value):
        for index, node in enumerate(self._nodes()):
            if node.value == value:
                return index
        return -1

    def to_list(self):
        return [node.value for node in self._nodes()]


class DNode(SNode):
    def __init__(self, value, previous=None, next_node=None):
        super().__init__(value, next_node)
        self.prev = previous


class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def prepend(self, value):
        node = DNode(value, next_node=self.head)
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node
        self.head = node
        self.size += 1

    def append(self, value):
        node = DNode(value, previous=self.tail)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def _remove(self, previous, node):
        if node.next is None:
            self.tail = previous
        else:
            node.next.prev = previous
        return super()._remove(previous, node)

    def delete_last(self):
        if self.tail is None:
            raise IndexError("Siyahı boşdur.")
        return self._remove(self.tail.prev, self.tail)

    def to_list_reverse(self):
        values = []
        node = self.tail
        while node is not None:
            values.append(node.value)
            node = node.prev
        return values
