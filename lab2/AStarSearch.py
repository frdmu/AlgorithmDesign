import math
import heapq
import numpy as np
from tool import *

def singleAStarSearch(Map, start, end):
    visited = np.zeros(Map.shape)    
    heap = []
    n = node(None, start, 0, end)
    while (n.x == end.x and n.y == end.y) == False:
        x_start = n.x - 1 if n.x - 1 >= 0 else n.x
        x_end = n.x + 1 if n.x + 1 < Map.shape[0] else n.x
        y_start = n.y - 1 if n.y - 1 >= 0 else n.y
        y_end = n.y + 1 if n.y + 1 < Map.shape[1] else n.y
        for i in range(x_start, x_end+1):
            for j in range(y_start, y_end+1):
                if (n.x == i and n.y == j) or Map[i][j] == -1 or visited[i][j] == 1: continue
                heapq.heappush(heap, node(n, point(i, j), Map[i][j], end))
                visited[i][j] = 1 
        if len(heap) == 0: return None 
        n = heapq.heappop(heap)
    return n

def bidirectionalAStarSearch(Map, start, end):
    visited, visitedReverse = np.zeros(Map.shape), np.zeros(Map.shape)
    heap, heapReverse = [node(None, start, 0, end)], [node(None, end, Map[end.x][end.y], start, 1)]
    n = heapq.heappop(heap) if heap[0] < heapReverse[0] else heapq.heappop(heapReverse)
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
                    heapq.heappush(heap, node(n, point(i, j), Map[i][j], end))
                    visited[i][j] = 1 
        else:
            if visited[n.x][n.y] == 1: break
            x_start = n.x - 1 if n.x - 1 >= 0 else n.x
            x_end = n.x + 1 if n.x + 1 < Map.shape[0] else n.x
            y_start = n.y - 1 if n.y - 1 >= 0 else n.y
            y_end = n.y + 1 if n.y + 1 < Map.shape[1] else n.y
            for i in range(x_start, x_end+1):
                for j in range(y_start, y_end+1):
                    if (n.x == i and n.y == j) or Map[i][j] == -1 or visitedReverse[i][j] == 1: continue
                    heapq.heappush(heapReverse, node(n, point(i, j), Map[i][j], start, 1))
                    visitedReverse[i][j] = 1 
        if len(heap) == 0 or len(heapReverse) == 0: return None, None 
        n = heapq.heappop(heap) if heap[0] < heapReverse[0] else heapq.heappop(heapReverse)
    if n.reverse == 0:
        for m in heapReverse:
            if (m.x == n.x) and (m.y == n.y):
                return n, m
    else:
        for m in heap:
            if (m.x == n.x) and (m.y == n.y):
                return m, n
