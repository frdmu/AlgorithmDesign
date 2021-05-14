from tool import *
from greedySetCover import *
from lpSetCover import *

if __name__  == '__main__':
    N, M = 5000, 20 
    X, F = generateDataSet(N, M)

    C1 = greedySetCover(X, F)
    printResult(X, F, C1, 0)

    C2 = lpSetCover(X, F)
    printResult(X, F, C2, 1)
