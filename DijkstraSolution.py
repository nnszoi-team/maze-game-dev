from queue import PriorityQueue

from printMap import edge, node

# 在此处引用头文件

row = 0
column = 0
counts = 0
srtx = 0
srty = 0
finx = 0
finy = 0
edges = []
distance = []
inQueue = []
prev = []
turn = "Down"
INF = 998244353


def readFile():
    global edges, distance, inQueue, prev
    global row, column, counts, srtx, srty, finx, finy
    f = open("Maze.out", "r")
    row, column = [int(i) for i in f.readline().split()]
    counts = int(f.readline())
    srtx, srty, finx, finy = [int(i) for i in f.readline().split()]
    for j in range(counts):
        x1, y1, x2, y2 = [int(i) for i in f.readline().split()]
        start = node(x1, y1)
        end = node(x2, y2)
        edges.append(edge(start, end))

    for i in range(row):
        dist = []
        idx = []
        prever = []
        for j in range(column):
            dist.append(INF)
            idx.append(False)
            prever.append(node())
        distance.append(dist)
        inQueue.append(idx)
        prev.append(prever)
    f.close()


def dijkstra():
    global edges, distance, inQueue, prev
    global row, column, counts, srtx, srty, finx, finy
    priQueue = PriorityQueue()
    distance[srtx][srty] = 0
    priQueue.put((0, node(srtx, srty)))
    while priQueue.empty() == False:
        value = priQueue.get()[1]
        if inQueue[value.x][value.y] == True:
            continue
        inQueue[value.x][value.y] = True
        for element in edges:
            if element.dx == value:
                if (
                    distance[element.dy.x][element.dy.y]
                    > distance[element.dx.x][element.dx.y] + 1
                ):
                    prev[element.dy.x][element.dy.y] = value
                    distance[element.dy.x][element.dy.y] = (
                        distance[element.dx.x][element.dx.y] + 1
                    )
                    if inQueue[element.dy.x][element.dy.y] == False:
                        priQueue.put(
                            (int(distance[element.dy.x][element.dy.y]), element.dy)
                        )
            if element.dy == value:
                if (
                    distance[element.dx.x][element.dx.y]
                    > distance[element.dy.x][element.dy.y] + 1
                ):
                    prev[element.dx.x][element.dx.y] = value
                    distance[element.dx.x][element.dx.y] = (
                        distance[element.dy.x][element.dy.y] + 1
                    )
                    if inQueue[element.dx.x][element.dx.y] == False:
                        priQueue.put(
                            (int(distance[element.dx.x][element.dx.y]), element.dx)
                        )
    # for i in range(column):
    # for j in range(row):
    # print(distance[j][i], end=" ")
    # print()


def findWay():
    global edges, distance, inQueue, prev
    global row, column, counts, srtx, srty, finx, finy
    ways = []
    dx = finx
    dy = finy
    while dx != srtx or dy != srty:
        ways.append(node(dx, dy))
        now = prev[dx][dy]
        dx = now.x
        dy = now.y
        pass
    ways.reverse()
    for element in ways:
        if element.x == dx - 1:
            moveLeft()
        if element.x == dx + 1:
            moveRight()
        if element.y == dy - 1:
            moveUp()
        if element.y == dy + 1:
            moveDown()
        dx = element.x
        dy = element.y


readFile()
dijkstra()
findWay()
#Main.run(Main.characters[0])
