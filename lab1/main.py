import time
from tool import *
from enumeration import *
from grahamScan import *
from divideConquer import *
if __name__ == '__main__':
    X, Y1, Y2, Y3 = [], [], [], []  
    for N in range (1000, 11000, 1000):
        Q = pointSet(N);
        X.append(N)
        print(N) 
        startTime = time.time()

        # enumeration 
        boundaryPointSet1 = enumeration(Q);
        endTime1 = time.time() 
        # drawPoint(Q, boundaryPointSet1, 1)
        # print(endTime1 - startTime)    
        
        # grahamScan 
        boundaryPointSet2 = grahamScan(Q);
        endTime2 = time.time()
        # print(endTime2 - endTime1)
        # drawPoint(Q, boundaryPointSet2, 2)
        
        # divideConquer
        boundaryPointSet3 = divideConquer(Q)
        endTime3 = time.time()
        # print(endTime3 - endTime2)
        # drawPoint(Q, boundaryPointSet3, 3)
        
        Y1.append(endTime1 - startTime) 
        Y2.append(endTime2 - endTime1)
        Y3.append(endTime3 - endTime2)

    drawPerformancePicture(X, Y1, Y2, Y3) 
