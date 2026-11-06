class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = {}

    def get(self, key: int) -> int:
        if key in self.dictionary:
            value = self.dictionary[key]
            self.dictionary.pop(key)
            self.dictionary[key] = value
            return self.dictionary[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.dictionary.pop(key)
        self.dictionary[key] = value
        if len(self.dictionary) > self.capacity:
            self.dictionary.pop(next(iter(self.dictionary)))

