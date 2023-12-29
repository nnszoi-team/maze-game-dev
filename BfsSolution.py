from queue import Queue
import pygame
import time

from visualizer import Node, Edge, Visualizer, image, BLOCK_WIDTH


row = 0
column = 0
edges = []
vis = []
srtx = 0
srty = 0
finx = 0
finy = 0


# 在此部分定义变量


def readFile():
    global row, column, edges, vis
    global srtx, srty, finx, finy
    f = open("maze.out", "r")
    row, column = [int(i) for i in f.readline().split()]
    for j in range(row):
        line = []
        value = []
        for i in range(column):
            line.append([])
            value.append(False)
        edges.append(line)
        vis.append(value)
    counts = int(f.readline())
    srtx, srty, finx, finy = [int(i) for i in f.readline().split()]
    for j in range(counts):
        x1, y1, x2, y2 = [int(i) for i in f.readline().split()]
        start = Node(x1, y1)
        endl = Node(x2, y2)
        edges[x1][y1].append(endl)
        edges[x2][y2].append(start)
    f.close()


def bfs():
    global row, column, edges, vis
    global srtx, srty, finx, finy
    Main.moveInterval = 0.01
    que = Queue()
    que.put(Main.characters[0])
    stayer = Queue()
    while que.empty() == False:
        copyQue = que
        while copyQue.empty() == False:
            now = que.get()
            if vis[now.x][now.y] == True:
                continue
            vis[now.x][now.y] = True
            available = 0
            if now.x == finx and now.y == finy:
                stayer.put(now)
                break
            for edge in edges[now.x][now.y]:
                if vis[edge.x][edge.y]:
                    continue
                available += 1
                spawnNewCharacter(now.x, now.y)
                Main.prev[edge.x][edge.y] = now
                if edge.x == now.x - 1:
                    moveLeft(len(Main.characters) - 1, False, False)
                elif edge.x == now.x + 1:
                    moveRight(len(Main.characters) - 1, False, False)
                elif edge.y == now.y - 1:
                    moveUp(len(Main.characters) - 1, False, False)
                elif edge.y == now.y + 1:
                    moveDown(len(Main.characters) - 1, False, False)
                que.put(Main.characters[len(Main.characters) - 1])
            if available == 0 or (now.x == finx and now.y == finy):
                stayer.put(now)
        Main.characters.clear()
        copyQue = que
        newImage = pygame.image.load("endl.png").convert()
        newImage = pygame.transform.scale(newImage, (BLOCK_WIDTH, BLOCK_WIDTH))
        while copyQue.empty() == False:
            Main.characters.append(copyQue.get())
        Main.screen.blit(
            newImage,
            (
                finx * 2 * BLOCK_WIDTH + BLOCK_WIDTH,
                finy * 2 * BLOCK_WIDTH + BLOCK_WIDTH,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                finx * 2 * BLOCK_WIDTH + BLOCK_WIDTH,
                finy * 2 * BLOCK_WIDTH + BLOCK_WIDTH,
                BLOCK_WIDTH,
                BLOCK_WIDTH,
            )
        )

    Main.characters.clear()
    while stayer.empty() == False:
        newImage = pygame.image.load("character.png").convert()
        newImage = pygame.transform.scale(newImage, (BLOCK_WIDTH, BLOCK_WIDTH))
        value = stayer.get()
        Main.screen.blit(
            newImage,
            (
                value.x * 2 * BLOCK_WIDTH + BLOCK_WIDTH,
                value.y * 2 * BLOCK_WIDTH + BLOCK_WIDTH,
            ),
        )
        Main.characters.append(value)
        pygame.display.update(
            pygame.Rect(
                value.x * 2 * BLOCK_WIDTH + BLOCK_WIDTH,
                value.y * 2 * BLOCK_WIDTH + BLOCK_WIDTH,
                BLOCK_WIDTH,
                BLOCK_WIDTH,
            )
        )


# 在此部分定义函数


# Main是对背景进行操作的一个类，其中储存有一个位于起点的节点characters[0]，你可以通过以下函数进行操作：
# Main.characters[0].characMoveUp()用于向上移动一格
# Main.characters[0].MoveDown()用于向下移动一格
# Main.characters[0].MoveLeft()用于向左移动一格
# Main.characters[0].MoveRight()用于向右移动一格
# Main.spawnNewCharacter(x,y)用于生成一个新的在(x,y)的节点
# 请注意！如果你对点移动的操作不可执行（即撞墙），则程序将会直接退出！
# 以下为主函数，请先调用Main.init()，在你的操作结束之后执行Main.run()进行检查
readFile()
bfs()
ans = 0
for i in range(len(Main.characters)):
    if Main.characters[i].x == finx and Main.characters[i].y == finy:
        ans = i
        break
print(ans)
