class ArrayStack:  # stack with fixed length
    def __init__(self, length):
        self.length = length
        self.array = []

    def push(self, value):
        if len(self.array) == self.length:
            print("full")
        else:
            self.array.append(value)

    def pop(self):
        if len(self.array) == 0:
            print("empty")
            return None
        else:
            return self.array.pop()

    def peek(self):
        return self.array[len(self.array) - 1] if len(self.array) != 0 else None


if __name__ == "__main__":
    stack = ArrayStack(3)
    print(stack.array)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.array)
    stack.push(4)
    a = stack.pop()
    b = stack.pop()
    c = stack.pop()
    d = stack.pop()
    print(a, b, c, d)
    stack.push(100)
    stack.push(200)
    print(stack.array)