class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Link:
    def __init__(self):
        self.head = None

    def append(self, value):
        new = Node(value)
        p = self.head
        if p is None:
            self.head = new
        else:
            while p.next:
                p = p.next
            p.next = new

    def print_link(self):
        p = self.head
        while p:
            print(p.data, end=" ")
            p = p.next
        print()

    def reverse_link(self):
        pre = None
        lat = None
        while self.head:
            lat = self.head.next
            self.head.next = pre
            pre = self.head
            self.head = lat
        self.head = pre


link = Link()
for i in range(1, 10):
    link.append(i)

link.print_link()

link.reverse_link()
link.print_link()

