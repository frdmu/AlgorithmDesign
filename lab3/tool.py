import random

def generateDataSet(N, M):
    X = [i for i in range(1, N + 1)]
    F = dict()
    F['S0'] = random.sample(X, M)
    F['S0'].sort()
    U = set(F['S0'])
    j = 1
    # make sure the feasible solution
    while True:
        Y = list(set(X).difference(U))  # X-U
        if len(Y) < M:
            F['S' + str(j)] = Y
            j += 1
            break
        n = random.randint(1, M)
        x = random.randint(1, n)
        F['S' + str(j)] = random.sample(Y, x) + random.sample(list(U), n - x)
        F['S' + str(j)].sort()
        U = U.union(set(F['S' + str(j)]))
        j += 1
    # make F up (because j must be less than N)
    while j < N:
        n = random.randint(1, M)
        F['S' + str(j)] = random.sample(X, n)
        F['S' + str(j)].sort()
        j += 1
    return X, F

def printResult(X: list, F: dict, C: list, flag) -> None:
    U = set()
    for key in C:
        # uncover:
        uncover = list(set(X).difference(U))
        uncover.sort()
        # print("uncover:", end='')
        # print(uncover)
        # select
        S = F[key]
        # print(str(key) + ":", end='')
        # print(S)
        # new cover
        # print("new cover:", end='')
        add = list(set(S).difference(U))
        add.sort()
        # print(add)
        U = U.union(set(S))
    print("+" * 40)
    print("The number of dataset is:", len(X))
    print("+" * 40) 
    if flag == 0:
        print("Solution of greedy is C:")
    else:
        print("Solution of linear programming is C:")
    print(C)
    print("*" * 80)
    print("Len of union of C:")
    U = list(U)
    U.sort()
    print(len(U))
    print("*" * 80)
    print("Len of X:")
    print(len(X))
    print("*" * 80)
