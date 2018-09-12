class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.random = None


def copy_deep(head):
    new2old = dict()
    cur = head
    while cur:
        new2old[cur] = Node(cur.value)
        cur = cur.next
    cur = head
    while cur:
        new2old[cur].next = cur.next
        new2old[cur].random = cur.random
        cur = cur.next
    return new2old[head]


def print_link(head):
    cur = head
    print("next link: ", end=" ")
    while cur:
        print(cur.value, end=" ")
        cur = cur.next
    print("\nrandom link")
    cur = head
    while cur:
        print(str(cur.value) + " " + str(" " if cur.random is None else cur.random.value))
        cur = cur.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.random = head.next.next.next.next.next  # 1 -> 6
    head.next.random = head.next.next.next.next.next  # 2 -> 6
    head.next.next.random = head.next.next.next.next  # 3 -> 5
    head.next.next.next.random = head.next.next  # 4 -> 3
    head.next.next.next.next.random = None  # 5 -> null
    head.next.next.next.next.next.random = head.next.next.next  # 6 -> 4

    print_link(head)
    print()

    new_head = copy_deep(head)
    print_link(new_head)

    print()
    print_link(head)
