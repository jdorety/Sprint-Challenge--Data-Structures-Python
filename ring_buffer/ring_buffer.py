class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        if self.current == self.capacity - 1:
            self.current = 0
        else:
            self.current += 1
        print(self.storage)

    def get(self):
        current_storage = []
        for i in self.storage:
            if i is not None:
                current_storage.append(i)

        return current_storage
