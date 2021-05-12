from tool import *
from grahamScan import *
def divide(Q):
    Qlist = list(Q)
    n = len(Qlist)
    minX, maxX = 101, -1 
    for i in range(n):
        if (Qlist[i].x < minX):
            minX = Qlist[i].x
        if (Qlist[i].x > maxX):
            maxX = Qlist[i].x
    mediumX = (minX + maxX) / 2
    Ql = []
    Qr = []
    for i in range(n):
        if (Qlist[i].x < mediumX):
            Ql.append(Qlist[i])
        else:
            Qr.append(Qlist[i])
    return set(Ql), set(Qr)

def merge(Ql, CHl, CHr):
    if len(CHl) == 0:
        return CHr
    if len(CHr) == 0:
        return CHl
    if len(Ql) > len(CHl):
        p0 = list(Ql - CHl)[0]
        Q = CHl.union(CHr)
        for p in Q:
            if p.x == p0.x and p.y > p0.y:
                p.angle = math.pi / 2
            elif p.x == p0.x and p.y < p0.y:
                p.angle = math.pi / 2 * 3
            elif p.x > p0.x and p.y >= p0.y:
                p.angle = math.atan((p.y - p0.y) / (p.x - p0.x))
            elif p.x > p0.x and p.y < p0.y:
                p.angle = math.pi * 2 - math.atan((p0.y - p.y) / (p.x - p0.x))
            elif p.x < p0.x and p.y >= p0.y:
                p.angle = math.pi - math.atan((p.y - p0.y) / (p0.x - p.x)) 
            elif p.x < p0.x and p.y < p0.y:
                p.angle = math.pi + math.atan((p0.y - p.y) / (p0.x - p.x)) 
        Qlist = list(Q) 
        Qlist = sorted(Qlist, key = lambda point : (point.angle))
    else:
        Qlist = list(CHl.union(CHr))
    boundaryPointSet = grahamScan(set(Qlist)) 
    return boundaryPointSet

def divideAndConquer(Q):
    n = len(Q)
    if n < 3:
        return Q
    elif n == 3:
        Qlist, p0 = sortByAngle(Q) 
        return set([p0] + Qlist)
    Ql, Qr = divide(Q)
    if len(Ql) == 0: 
        return Qr
    if len(Qr) == 0:
        return Ql
    CHl = divideAndConquer(Ql)
    CHr = divideAndConquer(Qr)
    boundaryPointSet = merge(Ql, CHl, CHr)
    return boundaryPointSet

def divideConquer(Q):
    boundaryPointSet = divideAndConquer(Q)
    return boundaryPointSet
