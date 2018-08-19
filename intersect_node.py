# 两个单链表相交的一系列问题
# 题目:在本题中,单链表可能有环,也可能无环.给定两个单链表的头节点head1和head2,
# 这两个链表可能相交,也可能不相交. 请实现一个函数,如果两个链表相交,请返回相交的
# 第一个节点;如果不相交,返回null即可.要求:如果链表1的长度为N， 链表2的长度为M，
# 时间复杂度请达到 O(N+M)， 额外空间复杂度请达到O(1)。


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def get_loop_node(head):
    fast = head
    slow = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
    return None


def get_intersect_node(head1, head2):
    head_1_loop_node = get_loop_node(head1)
    head_2_loop_node = get_loop_node(head2)
    if head_1_loop_node is None and head_2_loop_node is None:
        no_loop(head1, head2)
    elif head_1_loop_node is not None and head_2_loop_node is not None:
        both_loop(head1, head_1_loop_node, head2, head_2_loop_node)
    else:
        return None


def no_loop(head1, head2):
    cursor1, cursor2 = head1, head2
    len1, len2 = 1, 1
    while cursor1.next:
        cursor1, len1 = cursor1.next, len1 + 1
    while cursor2.next:
        cursor2, len2 = cursor2.next, len2 + 1

    if cursor1 != cursor2:
        return None
    else:
        (cursor1, cursor2) = (head1, head2) if len1 < len2 else (head2, head1)
        count = 0
        while count < abs(len1 - len2):
            cursor2 = cursor2.next
            count += 1
        while cursor2 != cursor1:
            cursor2 = cursor2.next
            cursor1 = cursor1.next
        return cursor2


def both_loop(head1, head_1_loop_node, head2, head_2_loop_node):
    if head_1_loop_node == head_2_loop_node:
        cursor1, cursor2 = head1, head2
        len1, len2 = 1, 1
        while cursor1 != head_1_loop_node:
            cursor1, len1 = cursor1.next, len1 + 1
        while cursor2 != head_2_loop_node:
            cursor2, len2 = cursor2.next, len2 + 1

        (cursor1, cursor2) = (head1, head2) if len1 < len2 else (head2, head1)
        count = 0
        while count < abs(len1 - len2):
            cursor2 = cursor2.next
            count += 1
        while cursor2 != cursor1:
            cursor2 = cursor2.next
            cursor1 = cursor1.next
        return cursor2
    else:
        p = head_1_loop_node.next
        while p != head_1_loop_node:
            if p == head_2_loop_node:
                return head_2_loop_node
            p = p.next
        return None

if __name__ == "__main__":

    # check function get_loop_node
    # 1 -> 2 -> 3 -> 4 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    p = head
    while p:
        print(p.data, end=" ")
        p = p.next
    print()
    print("head has loop?", get_loop_node(head))

    # 1 -> 2 -> 3 -> 4 -> 5 -> 3
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = head1.next.next
    print("head1 has loop?", get_loop_node(head1).data)

    # check function no_loop
    # case 1: no loop, with intersection
    # head : 1 -> 2 -> 3 -> 4 -> None
    # head2 : 8 -> 7 -> 6 -> 5 -> 2 -> 3 -> 4 -> None
    head2 = Node(8)
    head2.next = Node(7)
    head2.next.next = Node(6)
    head2.next.next.next = Node(5)
    head2.next.next.next.next = head.next
    print("intersect node of head and head2: ", no_loop(head, head2).data)

    # case 2: no loop, no intersection
    # head: 1 -> 2 -> 3 -> 4 -> None
    # head3: 1 -> 2 -> 3 -> 4-> 5 -> None
    head3 = Node(1)
    head3.next = Node(2)
    head3.next.next = Node(3)
    head3.next.next.next = Node(4)
    head3.next.next.next.next = Node(5)
    print("intersect node of head and head3: ", no_loop(head, head3))

    # check function both_loop
    # case 1: with loop, no intersection
    # head1: 1 -> 2 -> 3 -> 4 -> 5 -> 3
    # head4: 100 -> 200 -> 300 -> 400 -> 300
    head4 = Node(100)
    head4.next = Node(200)
    head4.next.next = Node(300)
    head4.next.next.next = Node(400)
    head4.next.next.next.next = head4.next.next
    loop1 = get_loop_node(head1)
    loop4 = get_loop_node(head4)
    print("intersect node of head1 and head4: ", both_loop(head1, loop1, head4, loop4))

    # case 2: intersect node out of the loop
    # head1: 1 -> 2 -> 3 -> 4 -> 5 -> 3
    # head5: 7 -> 8 -> 9 -> 2 -> 3 -> 4 -> 5 -> 3
    head5 = Node(7)
    head5.next = Node(8)
    head5.next.next = Node(9)
    head5.next.next.next = head1.next
    loop5 = get_loop_node(head5)
    print("intersect node of head1 and head5: ", both_loop(head1, loop1, head5, loop5).data)

    # case 3:
    # head1: 1 -> 2 -> 3 -> 4 -> 5 -> 3
    # head6: 9 -> 8 -> 5 -> 3 -> 4 > 5
    head6 = Node(9)
    head6.next = Node(8)
    head6.next.next = head1.next.next.next.next
    loop6 = get_loop_node(head6)
    print("intersect node of head1 and head6: ", both_loop(head1, loop1, head6, loop6).data)