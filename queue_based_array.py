class ArrayQueue:
    def __init__(self, length):
        self.length = length
        self.array = [0] * self.length
        self.size = 0  # number of elements in the queue
        self.in_pointer = 0
        self.out_pointer = 0

    def push(self, value):
        if self.size == self.length:
            print("full")
        else:
            self.array[self.in_pointer] = value
            self.in_pointer = 0 if self.in_pointer == self.length - 1 else self.in_pointer + 1
            self.size += 1

    def pop(self):
        if self.size == 0:
            print("empty")
        else:
            value = self.array[self.out_pointer]
            self.out_pointer = 0 if self.out_pointer == self.length - 1 else self.out_pointer + 1
            self.size -= 1

    def print_queue(self):
        p = self.out_pointer
        temp = self.size
        while temp > 0:
            print(self.array[p], end=" ")
            p = p + 1 if p < self.length - 1 else 0
            temp -= 1
        print()


queue = ArrayQueue(3)
queue.print_queue()
queue.push(1)  # [1]
queue.push(2)  # [1, 2]
queue.push(3)  # [1, 2, 3]
queue.print_queue()
queue.push(4)  # full,
queue.pop()    # [2, 3]
queue.print_queue()
queue.push(5)  # [2, 3, 5]
queue.print_queue()
queue.push(6)  # full
queue.pop()    # [3, 5]
queue.print_queue()
queue.pop()    # [5]
queue.print_queue()
queue.pop()    # []
queue.print_queue()
queue.pop()