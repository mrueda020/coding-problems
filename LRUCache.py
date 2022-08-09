from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.deque = deque()

    def get(self, key: int) -> int:

        if key not in self.map:
            return -1
        else:
            value = self.map[key]

            self.deque.remove(key)
            self.deque.append(key)
            return value

    def put(self, key: int, value: int) -> None:

        if key not in self.map:

            if self.capacity == len(self.deque):

                oldest = self.deque.popleft()
                del self.map[oldest]

        else:
            self.deque.remove(key)

        self.map[key] = value
        self.deque.append(key)
