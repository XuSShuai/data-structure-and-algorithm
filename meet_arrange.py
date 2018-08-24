# 一些项目要占用一个会议室宣讲， 会议室不能同时容纳两个项目
# 的宣讲。 给你每一个项目开始的时间和结束的时间(给你一个数
# 组， 里面 是一个个具体的项目)， 你来安排宣讲的日程， 要求会
# 议室进行 的宣讲的场次最多。 返回这个最多的宣讲场次。


class Meet:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def best_meet_arrange(start, end, cur):
    meets = []
    for i in range(len(start)):
        meets.append(Meet(start[i], end[i]))
    meets_sort = sorted(meets, key=lambda x: x.end)
    meet_count = 0
    for i in range(len(start)):
        if cur <= meets_sort[i].start:
            meet_count += 1
            cur = meets_sort[i].end
    return meet_count

if __name__ == "__main__":
    start = [8, 9, 13, 15, 15.20]
    end = [10, 9.50, 14, 15.30, 16]
    # end   9.50 10 14 15.30 16
    # start 9    8  13 15    15.20
    print(best_meet_arrange(start, end, 8))