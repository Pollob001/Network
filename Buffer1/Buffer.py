class CircularBuffer(object):

    def __init__(self, max_size):
        self.buffer = [None] * max_size
        self.head = 0
        self.tail = 0
        self.max_size = max_size

    def __str__(self):
        items = ['{!r}'.format(item) for item in self.buffer]
        return '[' + ', '.join(items) + ']'

    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head
        return self.max_size - self.head - self.tail

    def is_empty(self):
        return self.tail == self.head

    def is_full(self):
        return self.tail == (self.head - 1) % self.max_size

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError(
                "CircularBuffer is full, unable to enqueue item")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size

    def front(self):
        return self.buffer[self.head]

    def dequeue(self):
        if self.is_empty():
            raise IndexError("CircularBuffer is empty, unable to dequeue")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return item

    def Size_off_BUFF(self):
        if self.tail >= self.head:
            return self.tail - self.head



# Examples
n = input('Enter the buffer size : ')
cb = CircularBuffer(int(n))
print("Buffer is Empty: {}".format(cb.is_empty()))
print("Buffer is Full: {}".format(cb.is_full()))
print("CUrrnet Status of buffer :" + (str(cb)))
print("ADDING element to the buffer: ")
cb.enqueue("one")
cb.enqueue("two")
cb.enqueue("three")
cb.enqueue("four")
print("After Adding Element :" + (str(cb)))
print(f'Left size buffer is : {cb.buffer.count(None)}')
print(f'Occupide size buffer is : {int(n) - int(cb.buffer.count(None))}')
print('---------')

print(cb.dequeue())
print(cb.dequeue())
print("After getting element :" + (str(cb)))
print(f'Left size buffer is : {cb.buffer.count(None)}')
print(f'Occupide size buffer is : {int(n) - int(cb.buffer.count(None))}')
print('---------')
cb.enqueue("five")
cb.enqueue("six")
print("Again Adding Element :" + (str(cb)))
print(f'Left size buffer is : {cb.buffer.count(None)}')
print(f'Occupide size buffer is : {int(n) - int(cb.buffer.count(None))}')
print('---------')
print("When Buffer is Full: {}".format(cb.is_full()))
