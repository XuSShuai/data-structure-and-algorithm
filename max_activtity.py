# 一个公司的上下节关系是一棵多叉树， 这个公司要举办晚会， 你作为组织者已经摸清了大家的心理： 一个员工的直
# 接上级如果到场， 这个员工肯定不会来。 每个员工都有一个活跃度的值， 决定谁来你会给这个员工发邀请函， 怎么
# 让舞会的气氛最活跃？ 返回最大的活跃值。


class Node:
    def __init__(self, activity):
        self.activity = activity
        self.nexts = []


class ReturnInfo:
    def __init__(self, c_activity, n_activity):
        self.c_activity = c_activity
        self.n_activity = n_activity


def get_max_activity(head):
    return_info = process(head)
    return return_info.c_activity if return_info.c_activity > return_info.n_activity else return_info.n_activity


def process(head):
    c_a = head.activity
    n_a = 0
    for i in range(len(head.nexts)):
        return_info = process(head.nexts[i])
        c_a += return_info.n_activity
        n_a += max([return_info.n_activity, return_info.c_activity])
    return ReturnInfo(c_a, n_a)

if __name__ == "__main__":
    # head = Node(20)
    head = Node(10)
    head.nexts.append(Node(2))
    head.nexts.append(Node(7))
    head.nexts.append(Node(20))
    head.nexts[0].nexts.append(Node(6))
    head.nexts[0].nexts.append(Node(7))
    head.nexts[0].nexts.append(Node(8))
    head.nexts[1].nexts.append(Node(1))
    head.nexts[1].nexts.append(Node(2))
    head.nexts[2].nexts.append(Node(1))
    head.nexts[2].nexts.append(Node(2))
    head.nexts[2].nexts.append(Node(3))
    head.nexts[2].nexts.append(Node(4))

    print(get_max_activity(head))