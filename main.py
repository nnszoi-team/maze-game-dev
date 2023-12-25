import pygame, sys
import time
import os

from printMap import node, edge, background

from printMap import screenWidth, screenHeight, blockWidth, background_color


class character:
    def __init__(self, parent=None, x=0, y=0):
        self.parent = parent
        self.x = x
        self.y = y

    def moveUp(self, updated=True, cleared=True):
        if self.y == 0:
            return self.parent.demoQuit()
        checker = pygame.Rect(
            self.x * 2 * blockWidth + blockWidth,
            self.y * 2 * blockWidth + blockWidth,
            blockWidth,
            blockWidth,
        )

        if cleared == True:
            self.parent.screen.fill(background_color, checker)
            pygame.display.update(
                pygame.Rect(
                    self.x * 2 * blockWidth + blockWidth,
                    self.y * 2 * blockWidth + blockWidth,
                    blockWidth,
                    blockWidth,
                )
            )

        newImage = pygame.image.load("character.png").convert()
        newImage = pygame.transform.scale(newImage, (blockWidth, blockWidth))

        beginner = node(self.x, self.y)
        ender = node(self.x, self.y - 1)
        IsNotFind = True
        for line in self.parent.edges:
            if (line.dx == beginner and line.dy == ender) or (
                line.dy == beginner and line.dx == ender
            ):
                IsNotFind = False
                break
        if IsNotFind:
            # print('!')
            return self.parent.demoQuit()
        
        if self.parent.prev[self.x][self.y-1] == node(0,0):
            self.parent.prev[self.x][self.y-1]=node(self.x,self.y)

        self.parent.screen.blit(
            newImage,
            (
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth,
            ),
        )
        # pygame.display.flip()
        pygame.display.update(
            pygame.Rect(
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth,
                blockWidth,
                blockWidth,
            )
        )
        time.sleep(self.parent.moveInterval)
        if pygame.event.peek(pygame.QUIT):
            pygame.quit()
            sys.exit()

        if cleared == True:
            self.parent.screen.fill(
                background_color,
                (
                    self.x * 2 * blockWidth + blockWidth,
                    self.y * 2 * blockWidth,
                    blockWidth,
                    blockWidth,
                ),
            )
        pygame.display.update(
            pygame.Rect(
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth,
                blockWidth,
                blockWidth,
            )
        )
        # pygame.display.flip()

        self.y -= 1
        self.parent.screen.blit(
            newImage,
            (
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth + blockWidth,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth + blockWidth,
                blockWidth,
                blockWidth,
            )
        )
        # if updated:
        # pygame.display.flip()
        time.sleep(self.parent.moveInterval)
        if pygame.event.peek(pygame.QUIT):
            pygame.quit()
            sys.exit()

    def moveDown(self, updated=True, cleared=True):
        if self.y == self.parent.column - 1:
            return self.parent.demoQuit()

        checker = pygame.Rect(
            self.x * 2 * blockWidth + blockWidth,
            self.y * 2 * blockWidth + blockWidth,
            blockWidth,
            blockWidth,
        )

        if cleared == True:
            self.parent.screen.fill(background_color, checker)
            pygame.display.update(
                pygame.Rect(
                    self.x * 2 * blockWidth + blockWidth,
                    self.y * 2 * blockWidth + blockWidth,
                    blockWidth,
                    blockWidth,
                )
            )

        newImage = pygame.image.load("character.png").convert()
        newImage = pygame.transform.scale(newImage, (blockWidth, blockWidth))

        beginner = node(self.x, self.y)
        ender = node(self.x, self.y + 1)
        IsNotFind = True
        for line in self.parent.edges:
            if (line.dx == beginner and line.dy == ender) or (
                line.dy == beginner and line.dx == ender
            ):
                IsNotFind = False
                break
        if IsNotFind:
            return self.parent.demoQuit()
        
        if self.parent.prev[self.x][self.y+1] == node(0,0):
            self.parent.prev[self.x][self.y+1]=node(self.x,self.y)

        self.y += 1
        self.parent.screen.blit(
            newImage,
            (
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth,
                blockWidth,
                blockWidth,
            )
        )
        time.sleep(self.parent.moveInterval)

        if cleared == True:
            self.parent.screen.fill(
                background_color,
                (
                    self.x * 2 * blockWidth + blockWidth,
                    self.y * 2 * blockWidth,
                    blockWidth,
                    blockWidth,
                ),
            )
        pygame.display.update(
            pygame.Rect(
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth,
                blockWidth,
                blockWidth,
            )
        )

        self.parent.screen.blit(
            newImage,
            (
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth + blockWidth,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth + blockWidth,
                blockWidth,
                blockWidth,
            )
        )
        # if updated:
        # pygame.display.flip()
        time.sleep(self.parent.moveInterval)
        if pygame.event.peek(pygame.QUIT):
            pygame.quit()

    def moveLeft(self, updated=True, cleared=True):
        if self.x == 0:
            return self.parent.demoQuit()
        # print('?')
        checker = pygame.Rect(
            self.x * 2 * blockWidth + blockWidth,
            self.y * 2 * blockWidth + blockWidth,
            blockWidth,
            blockWidth,
        )
        if cleared == True:
            self.parent.screen.fill(background_color, checker)
            pygame.display.update(
                pygame.Rect(
                    self.x * 2 * blockWidth + blockWidth,
                    self.y * 2 * blockWidth + blockWidth,
                    blockWidth,
                    blockWidth,
                )
            )

        newImage = pygame.image.load("character.png").convert()
        newImage = pygame.transform.scale(newImage, (blockWidth, blockWidth))

        beginner = node(self.x, self.y)
        ender = node(self.x - 1, self.y)
        IsNotFind = True
        for line in self.parent.edges:
            if (line.dx == beginner and line.dy == ender) or (
                line.dy == beginner and line.dx == ender
            ):
                IsNotFind = False
                break
        if IsNotFind:
            return self.parent.demoQuit()
        
        if self.parent.prev[self.x-1][self.y]== node(0,0):
            self.parent.prev[self.x-1][self.y]=node(self.x,self.y)

        self.parent.screen.blit(
            newImage,
            (
                self.x * 2 * blockWidth,
                self.y * 2 * blockWidth + blockWidth,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                self.x * 2 * blockWidth,
                self.y * 2 * blockWidth + blockWidth,
                blockWidth,
                blockWidth,
            )
        )
        time.sleep(self.parent.moveInterval)

        if cleared == True:
            self.parent.screen.fill(
                background_color,
                (
                    self.x * 2 * blockWidth,
                    self.y * 2 * blockWidth + blockWidth,
                    blockWidth,
                    blockWidth,
                ),
            )
        pygame.display.update(
            pygame.Rect(
                self.x * 2 * blockWidth,
                self.y * 2 * blockWidth + blockWidth,
                blockWidth,
                blockWidth,
            )
        )

        self.x -= 1
        self.parent.screen.blit(
            newImage,
            (
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth + blockWidth,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth + blockWidth,
                blockWidth,
                blockWidth,
            )
        )
        # if updated:
        # pygame.display.flip()
        time.sleep(self.parent.moveInterval)
        if pygame.event.peek(pygame.QUIT):
            pygame.quit()
            sys.exit()

    def moveRight(self, updated=True, cleared=True):
        if self.x == self.parent.row - 1:
            return self.parent.demoQuit()
        checker = pygame.Rect(
            self.x * 2 * blockWidth + blockWidth,
            self.y * 2 * blockWidth + blockWidth,
            blockWidth,
            blockWidth,
        )
        if cleared == True:
            self.parent.screen.fill(background_color, checker)
            pygame.display.update(
                pygame.Rect(
                    self.x * 2 * blockWidth + blockWidth,
                    self.y * 2 * blockWidth + blockWidth,
                    blockWidth,
                    blockWidth,
                )
            )

        newImage = pygame.image.load("character.png").convert()
        newImage = pygame.transform.scale(newImage, (blockWidth, blockWidth))

        beginner = node(self.x, self.y)
        ender = node(self.x + 1, self.y)
        IsNotFind = True
        for line in self.parent.edges:
            if (line.dx == beginner and line.dy == ender) or (
                line.dy == beginner and line.dx == ender
            ):
                IsNotFind = False
                break
        if IsNotFind:
            # print('!!!')
            return self.parent.demoQuit()
        
        if self.parent.prev[self.x+1][self.y] == node(0,0):
            self.parent.prev[self.x+1][self.y]=node(self.x,self.y)

        self.x += 1
        self.parent.screen.blit(
            newImage,
            (
                self.x * 2 * blockWidth,
                self.y * 2 * blockWidth + blockWidth,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                self.x * 2 * blockWidth,
                self.y * 2 * blockWidth + blockWidth,
                blockWidth,
                blockWidth,
            )
        )
        time.sleep(self.parent.moveInterval)

        if cleared == True:
            self.parent.screen.fill(
                background_color,
                (
                    self.x * 2 * blockWidth,
                    self.y * 2 * blockWidth + blockWidth,
                    blockWidth,
                    blockWidth,
                ),
            )
        pygame.display.update(
            pygame.Rect(
                self.x * 2 * blockWidth,
                self.y * 2 * blockWidth + blockWidth,
                blockWidth,
                blockWidth,
            )
        )

        self.parent.screen.blit(
            newImage,
            (
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth + blockWidth,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                self.x * 2 * blockWidth + blockWidth,
                self.y * 2 * blockWidth + blockWidth,
                blockWidth,
                blockWidth,
            )
        )
        # if updated:
        # pygame.display.flip()
        time.sleep(self.parent.moveInterval)
        if pygame.event.peek(pygame.QUIT):
            pygame.quit()
            sys.exit()

    def clears(self):
        self.parent.screen.fill(
            background_color, (self.x, self.y, blockWidth, blockWidth)
        )


class BackMap:
    def __init__(self, moveInterval=0.1):
        self.row = 0
        self.column = 0
        self.counts = 0
        self.edges = []
        self.blocks = []
        self.srtx = 0
        self.srty = 0
        self.finx = 0
        self.finy = 0
        self.moveInterval = moveInterval
        self.characters = []
        self.prev=[]

        self.screen = None

        self.backGround = background(
            self.screen, self.srtx, self.srty, self.finx, self.finy, []
        )
        # character = pygame.Rect(0, 0, blockWidth, blockWidth)
        # end = pygame.Rect(0, 0, blockWidth, blockWidth)

    def readFile(self):
        f = open("maze.out", "r")
        self.row, self.column = [int(i) for i in f.readline().split()]
        self.counts = int(f.readline())
        self.srtx, self.srty, self.finx, self.finy = [
            int(i) for i in f.readline().split()
        ]
        for i in range(self.row):
            prever=[]
            for j in range(self.column):
                prever.append(node())
            self.prev.append(prever)
            
        for j in range(self.counts):
            x1, y1, x2, y2 = [int(i) for i in f.readline().split()]
            start = node(x1, y1)
            endl = node(x2, y2)
            self.edges.append(edge(start, endl))
            # print(x1,y1,x2,y2)
            # print((x1+x2)*blockWidth,(y1+y2)*blockWidth)

            # for element in edges:
            # print(element.dx.x,element.dx.y,element.dy.x,element.dy.y)
        f.close()

    def drawStarted(self):
        newImage = pygame.image.load("endl.png").convert()
        newImage = pygame.transform.scale(newImage, (blockWidth, blockWidth))
        self.screen.blit(
            newImage,
            (self.srtx * 2* blockWidth + blockWidth, self.srty * 2* blockWidth + blockWidth),
        )
        pygame.display.update(
            pygame.Rect(
                self.srtx * 2* blockWidth + blockWidth,
                self.srty * 2* blockWidth + blockWidth,
                blockWidth,
                blockWidth,
            )
        )
        
    def drawWay(self):
        newImage = pygame.image.load("endl.png").convert()
        newImage = pygame.transform.scale(newImage, (blockWidth, blockWidth))
        dx = self.finx
        dy = self.finy
        while dx != self.srtx or dy != self.srty:
            self.screen.blit(
                newImage,
                (dx * 2 * blockWidth + blockWidth, dy * 2 * blockWidth + blockWidth),
            )
            pygame.display.update(
                pygame.Rect(
                    dx * 2 * blockWidth + blockWidth,
                    dy * 2 * blockWidth + blockWidth,
                    blockWidth,
                    blockWidth,
                )
            )
            time.sleep(0.05)
            last = self.prev[dx][dy]
            self.screen.blit(
                newImage, ((last.x + dx + 1) * blockWidth, (last.y + dy + 1) * blockWidth)
            )
            pygame.display.update(
                pygame.Rect(
                    (last.x + dx + 1) * blockWidth,
                    (last.y + dy + 1) * blockWidth,
                    blockWidth,
                    blockWidth,
                )
            )
            time.sleep(0.05)
            dx = last.x
            dy = last.y
        self.screen.blit(
            newImage,
            (self.srtx * 2 * blockWidth + blockWidth, self.srty * 2 * blockWidth + blockWidth),
        )
        pygame.display.update(
            pygame.Rect(
                self.srtx * 2 * blockWidth + blockWidth,
                self.srty * 2 * blockWidth + blockWidth,
                blockWidth,
                blockWidth,
            )
        )

    def demoQuit(self, txt="Runtime Error"):
        self.drawStarted()
        # return
        font = pygame.font.Font("consola.ttf", 100)
        # font.bold = True
        textSurface = font.render(txt, True, (255, 221, 85))
        self.drawWay()
        self.screen.blit(textSurface, (50, 50))
        pygame.display.flip()
        running = True
        while running:
            if pygame.event.peek(pygame.QUIT):
                running = False
        pygame.quit()

    def moveUp(self, idx=0, updated=True, cleared=True):
        self.characters[idx].moveUp(updated, cleared)
        self.drawStarted()

    def moveDown(self, idx=0, updated=True, cleared=True):
        self.characters[idx].moveDown(updated, cleared)
        self.drawStarted()

    def moveLeft(self, idx=0, updated=True, cleared=True):
        self.characters[idx].moveLeft(updated, cleared)
        self.drawStarted()

    def moveRight(self, idx=0, updated=True, cleared=True):
        self.characters[idx].moveRight(updated, cleared)
        self.drawStarted()

    def init(self, spawnNewMap=True):
        if spawnNewMap:
            os.system("CreateMap.exe")
        self.readFile()
        self.characters.append(character(self, self.srtx, self.srty))
        # backGround.drawEdge(row, column)

    def run(self, checker=character()):
        if checker.x != self.finx or checker.y != self.finy:
            return self.demoQuit("You Lose!")
        self.demoQuit("You Win!")

    def spawnNewCharacter(self, x=0, y=0):
        self.characters.append(character(self, x, y))

    def clears(self):
        self.screen.fill(background_color)
        self.init()
