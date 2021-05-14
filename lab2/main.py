from tool import *
from AStarSearch import *

if __name__ == '__main__':
    # singleAStarSearch on Map 1
    Map, start, end = getMap_1()
    path = singleAStarSearch(Map, start, end)
    if path:
        print("result of singleAStarSearch on Map_1 is:", path.f)
    else:
        print("singleAStarSearch on Map_1 has no answer")
    drawResult(Map, 1, start, end, [path])

    # singleAStarSearch on Map 2
    Map, start, end = getMap_2()
    path = singleAStarSearch(Map, start, end)
    if path:
        print("result of singleAStarSearch on Map_2 is:", path.f)
    else:
        print("singleAStarSearch on Map_2 has no answer")
    drawResult(Map, 2, start, end, [path])
    
    # bidirectionalAStarSearch on Map 1
    Map, start, end = getMap_1()
    pathStart, pathEnd = bidirectionalAStarSearch(Map, start, end)
    if pathStart and pathEnd:
        print("result of bidirectionalAStarSearch on Map_1 is:", pathStart.g + pathEnd.parent.g + math.sqrt((pathStart.x-pathEnd.parent.x)**2 + (pathStart.y-pathEnd.parent.y)**2))
    else:
        print("bidirectionalAStarSearch on Map_1 has no answer")
    drawResult(Map, 1, start, end, [pathStart, pathEnd])


    # bidirectionalAStarSearch on Map 2
    Map, start, end = getMap_2()
    pathStart, pathEnd = bidirectionalAStarSearch(Map, start, end)
    if pathStart and pathEnd:
        print("result of bidirectionalAStarSearch on Map_2 is:", pathStart.g + pathEnd.parent.g + math.sqrt((pathStart.x-pathEnd.parent.x)**2 + (pathStart.y-pathEnd.parent.y)**2))
    else:
        print("bidirectionalAStarSearch on Map_2 has no answer")
    drawResult(Map, 2, start, end, [pathStart, pathEnd])
