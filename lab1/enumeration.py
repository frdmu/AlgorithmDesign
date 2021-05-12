def inTriangle(p, a, b, c):
    """
    whether p in triangle formed by a, b, c 
    """
    signOfTriangle = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    signOfABP = (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x)
    signOfBCP = (c.x - b.x) * (p.y - b.y) - (c.y - b.y) * (p.x - b.x)
    signOfCAP = (a.x - c.x) * (p.y - c.y) - (a.y - c.y) * (p.x - c.x)
 
    flag1 = True if signOfTriangle * signOfABP > 0 else False 
    flag2 = True if signOfTriangle * signOfBCP > 0 else False
    flag3 = True if signOfTriangle * signOfCAP > 0 else False
    
    return flag1 & flag2 & flag3

def enumeration(Q):
    """
    Q: point set
    return boundaryPoint
    """
    n = len(Q)
    Qlist = list(Q)
    internalPointSet = set()
    
    m = Qlist[0]
    for p in Qlist:
        if p.x < m.x:
            m = p

    for i in range(0, n-2):
        if Qlist[i] in internalPointSet:
            continue
        for j in range(i+1, n-1):
            if Qlist[j] in internalPointSet:
                continue
            for k in range(j+1, n):
                if Qlist[k] in internalPointSet:
                    continue
                if inTriangle(Qlist[i], Qlist[j], Qlist[k], m): 
                    internalPointSet.add(Qlist[i]) 
                    break
                if inTriangle(Qlist[j], Qlist[i], m, Qlist[k]): 
                    internalPointSet.add(Qlist[j]) 
                    break
                if inTriangle(Qlist[k], Qlist[i], Qlist[j], m): 
                    internalPointSet.add(Qlist[k]) 
            if Qlist[i] in internalPointSet:
                    break
    return Q - internalPointSet # boundaryPointSet
