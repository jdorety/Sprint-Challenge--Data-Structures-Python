class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item # store value at current index
        if self.current == self.capacity - 1:
            self.current = 0  # Resets current index to beginning if currently at end index
        else:
            self.current += 1 # Increments to next index

    def get(self):
        return [item for item in self.storage if item != None]


# buffer = RingBuffer(3)

# print(buffer.get())   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# print(buffer.get())   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# print(buffer.get())   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# print(buffer.get())   # should return ['d', 'e', 'f']
