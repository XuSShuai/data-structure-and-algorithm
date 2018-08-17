import queue

stack = queue.LifoQueue(-1)
stack.put(1)
stack.put(2)
stack.put(3)

while not stack.empty():
    print(stack.get())

queue = queue.Queue(-1)
queue.put(1)
queue.put(2)
queue.put(3)

while not queue.empty():
    print(queue.get())