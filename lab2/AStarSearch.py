import math
import heapq
import numpy as np
from tool import *

def singleAStarSearch(Map, start, end):
    visited = np.zeros(Map.shape)    
    heap = []
    n = node(None, start, 0, end)
    visited[n.x][n.y] = 1
    while (n.x == end.x and n.y == end.y) == False:
        x_start = n.x - 1 if n.x - 1 >= 0 else n.x
        x_end = n.x + 1 if n.x + 1 < Map.shape[0] else n.x
        y_start = n.y - 1 if n.y - 1 >= 0 else n.y
        y_end = n.y + 1 if n.y + 1 < Map.shape[1] else n.y
        for i in range(x_start, x_end+1):
            for j in range(y_start, y_end+1):
                if (n.x == i and n.y == j) or Map[i][j] == -1 or visited[i][j] == 1: continue 
                
                flag = 0 
                for hNode in heap:
                    if hNode.x == i and hNode.y == j:
                       flag = 1
                       tmpNode = hNode
                       break
                if flag == 0: 
                    heapq.heappush(heap, node(n, point(i, j), Map[i][j], end))
                else:
                    g = n.g + math.sqrt((n.x - i)**2 + (n.y - j)**2) + Map[i][j]
                    h = math.sqrt((end.x - i)**2 + (end.y - j)**2)
                    f = g + h
                    if f < tmpNode.f:
                        heap.remove(tmpNode)
                        heapq.heappush(heap, node(n, point(i, j), Map[i][j], end))
        
        if len(heap) == 0: return None 
        n = heapq.heappop(heap)
        visited[n.x][n.y] = 1
    return n

def bidirectionalAStarSearch(Map, start, end):
    set1, set2 = [], []
    visited, visitedReverse = np.zeros(Map.shape), np.zeros(Map.shape)
    heap, heapReverse = [node(None, start, 0, end)], [node(None, end, Map[end.x][end.y], start, 1)]
    if heap[0] < heapReverse[0]:
        n = heapq.heappop(heap)
        visited[n.x][n.y] = 1
        set1.append(n)
    else:
        n = heapq.heappop(heapReverse)
        visitedReverse[n.x][n.y] = 1
        set2.append(n)
    while True:
        if n.reverse == 0: # from start to end
            if visitedReverse[n.x][n.y] == 1: break # search path finish
            x_start = n.x - 1 if n.x - 1 >= 0 else n.x
            x_end = n.x + 1 if n.x + 1 < Map.shape[0] else n.x
            y_start = n.y - 1 if n.y - 1 >= 0 else n.y
            y_end = n.y + 1 if n.y + 1 < Map.shape[1] else n.y
            for i in range(x_start, x_end+1):
                for j in range(y_start, y_end+1):
                    if (n.x == i and n.y == j) or Map[i][j] == -1 or visited[i][j] == 1: continue
                    flag1 = 0 
                    for hNode in heap:
                        if hNode.x == i and hNode.y == j:
                           flag1 = 1
                           tmpNode1 = hNode
                           break
                    if flag1 == 0: 
                        heapq.heappush(heap, node(n, point(i, j), Map[i][j], end))
                    else:
                        g = n.g + math.sqrt((n.x - i)**2 + (n.y - j)**2) + Map[i][j]
                        h = math.sqrt((end.x - i)**2 + (end.y - j)**2)
                        f = g + h
                        if f < tmpNode1.f:
                            heap.remove(tmpNode1)
                            heapq.heappush(heap, node(n, point(i, j), Map[i][j], end))
        else:
            if visited[n.x][n.y] == 1: break
            x_start = n.x - 1 if n.x - 1 >= 0 else n.x
            x_end = n.x + 1 if n.x + 1 < Map.shape[0] else n.x
            y_start = n.y - 1 if n.y - 1 >= 0 else n.y
            y_end = n.y + 1 if n.y + 1 < Map.shape[1] else n.y
            for i in range(x_start, x_end+1):
                for j in range(y_start, y_end+1):
                    if (n.x == i and n.y == j) or Map[i][j] == -1 or visitedReverse[i][j] == 1: continue
                    flag2 = 0 
                    for hNode in heapReverse:
                        if hNode.x == i and hNode.y == j:
                           flag2 = 1
                           tmpNode2 = hNode
                           break
                    if flag2 == 0: 
                        heapq.heappush(heapReverse, node(n, point(i, j), Map[i][j], start, 1))
                    else:
                        g = n.g + math.sqrt((n.x - i)**2 + (n.y - j)**2) + Map[i][j]
                        h = math.sqrt((start.x - i)**2 + (start.y - j)**2)
                        f = g + h
                        if f < tmpNode2.f:
                            heapReverse.remove(tmpNode2)
                            heapq.heappush(heapReverse, node(n, point(i, j), Map[i][j], start, 1))
        if len(heap) == 0 or len(heapReverse) == 0: 
            return None, None 
        if heap[0] < heapReverse[0]:
            n = heapq.heappop(heap)
            set1.append(n)
            visited[n.x][n.y] = 1
        else:
            n = heapq.heappop(heapReverse)
            set2.append(n)
            visitedReverse[n.x][n.y] = 1
    if n.reverse == 0:
        for m in set2:
            if (m.x == n.x) and (m.y == n.y):
                return n, m
    else:
        for m in set1:
            if (m.x == n.x) and (m.y == n.y):
                return m, n
