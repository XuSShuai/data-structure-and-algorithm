# 汉诺塔


def process(N, fro, to, help):
    if N == 1:
        print("move 1" + " from " + fro + " to " + to)
        return

    process(N - 1, fro, help, to)
    print("move " + str(N) + " from " + fro + " to " + to)
    process(N - 1, help, to, fro)

if __name__== "__main__":
    process(3, "左", "右", "中")