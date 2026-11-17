class HashTable:
    """Eyni indeksə düşən açarları bir siyahıda saxlayır."""

    def __init__(self, capacity=8, max_load=0.75):
        if capacity < 1 or max_load <= 0:
            raise ValueError("Tutum və doluluq həddi müsbət olmalıdır.")
        self.capacity = capacity
        self.max_load = max_load
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0
        self.resizes = 0

    def __len__(self):
        return self.size

    def _bucket(self, key):
        return self.buckets[hash(key) % self.capacity]

    def put(self, key, value):
        bucket = self._bucket(key)
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        if self.size / self.capacity > self.max_load:
            self._resize()

    def get(self, key, default=None):
        for stored_key, value in self._bucket(key):
            if stored_key == key:
                return value
        return default

    def contains(self, key):
        marker = object()
        return self.get(key, marker) is not marker

    def __contains__(self, key):
        return self.contains(key)

    def delete(self, key):
        bucket = self._bucket(key)
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                del bucket[index]
                self.size -= 1
                return True
        return False

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        for bucket in old_buckets:
            for key, value in bucket:
                self._bucket(key).append((key, value))
        self.resizes += 1

    def stats(self):
        used = sum(bool(bucket) for bucket in self.buckets)
        return {
            "entries": self.size,
            "buckets": self.capacity,
            "load factor": round(self.size / self.capacity, 3),
            "used buckets": used,
            "colliding entries": self.size - used,
            "longest chain": max(map(len, self.buckets)),
            "resizes": self.resizes,
        }

    def show(self):
        for index, bucket in enumerate(self.buckets):
            print(f"  [{index}] {bucket}")
