from tool import *

def judge(a, b, c):
    if (c.x - a.x) * (b.y - a.y) - (c.y - a.y) * (b.x - a.x) >= 0:
        return True
    else:
        return False


def grahamScan(Q):
    Qlist, p0 = sortByAngle(Q)

    n = len(Qlist)
    stack = []
    stack.append(p0)
    stack.append(Qlist[0])
    stack.append(Qlist[1])
    for i in range(2, n):
        while len(stack) > 2 and judge(stack[-2], stack[-1], Qlist[i]):
            stack.pop(-1)
        stack.append(Qlist[i])

    return set(stack)
