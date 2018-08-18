class Node:
    def __init__(self, data):
        self.data = data
        self.last = None
        self.next = None


class Link:
    def __init__(self):
        self.head = None

    def append(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new
            new.last = p

    def print(self):
        p = self.head
        while p.next:
            print(p.data, end=" ")
            p = p.next
        print(p.data, end="|")
        while p:
            print(p.data, end=" ")
            p = p.last
        print()

    def reverse_link(self):
        pre = None
        fol = None
        while self.head:
            fol = self.head.next
            self.head.next = pre
            self.head.last = fol
            pre = self.head
            self.head = fol

        self.head = pre


if __name__ == "__main__":
    link = Link()
    for i in [2, 4, 6, 15, 30]:
        link.append(i)
    link.print()

    link.reverse_link()
    link.print()
