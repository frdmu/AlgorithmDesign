def greedySetCover(X, F):
    U = set(X)
    C = [] 
    while len(U) > 0:
        coverMax, iMax = -1, -1 
        for i in F.keys():
            if i in C: continue
            cover = len(U.intersection(set(F[i])))
            if cover > coverMax: coverMax, iMax = cover, i
        U = U - set(F[iMax])
        C.append(iMax)
    return C 

