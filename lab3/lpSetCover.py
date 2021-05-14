from pulp import *

def lpSetCover(X, F):
    existed = dict()
    f = [0] * len(X)
    for key in F.keys():
        tmp = [0] * len(X) 
        for e in F[key]:
            tmp[e-1] = 1
            f[e-1] += 1
        existed[key] = tmp

    prob = LpProblem('lpSetCover', LpMinimize)
    Xs_vars = LpVariable.dicts("Xs_vars", F.keys(), 0, 1, cat=LpContinuous)
    # target function 
    prob += lpSum([Xs_vars[key] for key in F.keys()])
    # constraints 
    for e in X:
        prob += lpSum(existed[key][e-1] * Xs_vars[key] for key in F.keys()) >= 1.0
    prob.solve()
    
    C = []
    for key in F.keys():
        if Xs_vars[key].value() >= 1.0/max(f):
            C.append(key)

    return C
