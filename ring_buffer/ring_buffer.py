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

    def get(self):
        current_index = self.current
        current_storage = []
        for i in range(0, self.capacity):
            
            if current_index <= self.capacity - 1:
                current_storage.append(self.storage[current_index])
                current_index += 1
            else:
                current_index = 0
                current_storage.append(self.storage[current_index])
        return current_storage
