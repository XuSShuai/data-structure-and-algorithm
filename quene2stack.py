import queue


class Queue2Stack:
    def __init__(self):
        self.data = queue.Queue(-1)
        self.auxiliary = queue.Queue(-1)

    def push(self, value):
        self.data.put(value)

    def pop(self):
        if self.data.qsize() == 0:
            return None
        while self.data.qsize() > 1:
            self.auxiliary.put(self.data.get())
        result = self.data.get()
        self.data, self.auxiliary = self.auxiliary, self.data
        return result


stack = Queue2Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())

stack.push(100)
stack.push(200)
print(stack.pop())
print(stack.pop())
print(stack.pop())
