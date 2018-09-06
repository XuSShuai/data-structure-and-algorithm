import queue


class Stack2Queue:
    def __init__(self):
        self.data = queue.LifoQueue(-1)
        self.auxiliary = queue.LifoQueue(-1)

    def push(self, value):
        self.data.put(value)

    def pop(self):
        if self.data.qsize() == 0:
            return None
        while self.data.qsize() > 1:
            self.auxiliary.put(self.data.get())
        result = self.data.get()
        while self.auxiliary.qsize() > 0:
            self.data.put(self.auxiliary.get())
        return result


queue = Stack2Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)

print(queue.pop())
print(queue.pop())
print(queue.pop())

queue.push(100)
queue.push(200)

print(queue.pop())
print(queue.pop())
print(queue.pop())