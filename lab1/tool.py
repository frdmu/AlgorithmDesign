import random
import matplotlib.pyplot as plt
import math

class point:
    def __init__(self, x, y, angle):
        self.x, self.y, self.angle = x, y, angle

def pointSet(N):
    Q = set()
    while len(Q) < N:
        a = point(random.randint(0, 100), random.randint(0, 100), 0)
        Q.add(a)
    return Q

def crossProduct(A, B, P):
    return (B.x - A.x) * (P.y - A.y) - (B.y - A.y) * (P.x - A.x)

def sortByAngle(Q):
    p0 = point(101, 101, 0)
    for p in Q:
        if p.y < p0.y:
            p0 = p
        elif p.y == p0.y and p.x < p0.x:
            p0 = p

    Q.remove(p0)

    for p in Q:
        if p.x == p0.x:
            p.angle = math.pi / 2
        elif p.x > p0.x:
            p.angle = math.atan((p.y - p0.y) / (p.x - p0.x))
        elif p.x < p0.x:
            p.angle = math.atan((p0.x - p.x) / (p.y - p0.y)) + math.pi / 2
    Qlist = list(Q) 
    Qlist = sorted(Qlist, key = lambda point : (point.angle))
    
    return Qlist, p0

def drawPoint(Q, P, flag):
    plt.subplot() 
    if flag == 1:
        plt.title("enumeration")
    elif flag == 2:
        plt.title("grahamScan")
    else:
        plt.title("divideConquer")

    plt.xlim(xmax=110, xmin=-10)
    plt.ylim(ymax=110, ymin=-10)
    plt.xlabel("x")
    plt.ylabel("y")
    for q in Q - P:
        plt.plot(q.x, q.y, 'ro')
    for p in P:
        plt.plot(p.x, p.y, 'bs')
    
    Plist = list(P) 
    Plist = sorted(Plist, key = lambda point: (point.x, point.y))
    A = Plist[0]
    B = Plist[-1]
    del Plist[0]
    del Plist[-1]
    L, R = [], []
    L.append(A)
    for p in Plist:
        if crossProduct(A, B, p) > 0:
            L.append(p)
        else:
            R.append(p)
    L.append(B)
    L.reverse()
    R.extend(L)
    n = len(R)
    for i in range(n-1):
        plt.plot([R[i].x, R[i+1].x], [R[i].y, R[i+1].y], color='b')
    plt.plot([R[-1].x, R[0].x], [R[-1].y, R[0].y], color='b')
    
    plt.show()

def drawPerformancePicture(X, Y1, Y2, Y3):
    plt.subplot(121)
    plt.title("enumeration")
    plt.xlim(xmax=max(X)*1.1, xmin=0)
    plt.ylim(ymax=max(Y1)*1.1, ymin=0)
    plt.xlabel("number")
    plt.ylabel("time")
    plt.plot(X, Y1, label="Enumeration", color="red", marker=".")
    for i in range(len(X)):
        plt.text(X[i], Y1[i], '%.4f' % Y1[i], ha='center', va= 'bottom')
    
    plt.subplot(122)
    plt.title("Graham-Scan&DivideConquer")
    plt.xlim(xmax=max(X)*1.1, xmin=0)
    plt.ylim(ymax=max(max(Y2),max(Y3))*1.1, ymin=0)
    plt.xlabel("number")
    plt.ylabel("time")
    plt.plot(X, Y2, label="Graham-Scan", color="blue", marker="o")
    plt.plot(X, Y3, label="DivideConquer", color="black", marker="<")
    for i in range(len(X)):
        plt.text(X[i], Y2[i], '%.4f' % Y2[i],ha='center', va= 'bottom')
        plt.text(X[i], Y3[i], '%.4f' % Y3[i],ha='center', va= 'bottom') 
    plt.legend()
    plt.show() 
