class Array:
    """Sabit tutumlu massiv."""

    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError("Tutum mənfi ola bilməz.")
        self.capacity = capacity
        self.size = 0
        self._data = [None] * capacity

    def __len__(self):
        return self.size

    def get(self, index):
        if not 0 <= index < self.size:
            raise IndexError("İndeks massivdən kənardır.")
        return self._data[index]

    def _make_room(self):
        if self.size == self.capacity:
            raise OverflowError("Massiv doludur.")

    def append(self, value):
        self.insert(self.size, value)

    def insert(self, index, value):
        if not 0 <= index <= self.size:
            raise IndexError("İndeks massivdən kənardır.")
        self._make_room()
        for position in range(self.size, index, -1):
            self._data[position] = self._data[position - 1]
        self._data[index] = value
        self.size += 1

    def delete_at(self, index):
        value = self.get(index)
        for position in range(index, self.size - 1):
            self._data[position] = self._data[position + 1]
        self.size -= 1
        self._data[self.size] = None
        return value

    def search(self, value):
        for index in range(self.size):
            if self._data[index] == value:
                return index
        return -1

    def to_list(self):
        return self._data[:self.size]


class DynamicArray(Array):
    """Dolduqda böyüyən və boşaldıqda kiçilən massiv."""

    def __init__(self, capacity=4):
        super().__init__(max(1, capacity))
        self.resizes = 0

    def _resize(self, capacity):
        self._data = self.to_list() + [None] * (capacity - self.size)
        self.capacity = capacity
        self.resizes += 1

    def _make_room(self):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

    def delete_at(self, index):
        value = super().delete_at(index)
        if self.capacity > 4 and self.size <= self.capacity // 4:
            self._resize(max(4, self.capacity // 2))
        return value
