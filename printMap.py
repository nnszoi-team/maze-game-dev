import pygame
import os
import time

# from main import screenWidth,screenHeight,blockWidth,background_color


screenWidth = 1000
screenHeight = 800
background_color = (0, 0, 0)
blockWidth = 10

image = pygame.image.load("block.png")
image = pygame.transform.scale(image, (blockWidth, blockWidth))


class node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        pass

    def __hash__(self):
        return hash((self.x, self.y))


class edge:
    def __init__(self, x=node(), y=node()):
        self.dx = x
        self.dy = y


class background:
    def __init__(self, parent=None, edges=[], srtx=0, srty=0, finx=0, finy=0):
        self.parent = parent

        self.blocks = []
        self.edges = edges
        self.srtx = srtx
        self.srty = srty
        self.finx = finx
        self.finy = finy
        self.dictor = {}

    def drawEdge(self, row=0, column=0):
        for j in range(0, column):
            for i in range(0, row):
                self.blocks.append(
                    pygame.Rect(
                        i * 2 * blockWidth + blockWidth,
                        j * 2 * blockWidth + blockWidth,
                        blockWidth,
                        blockWidth,
                    )
                )
                self.dictor[
                    node(
                        i * 2 * blockWidth + blockWidth, j * 2 * blockWidth + blockWidth
                    )
                ] = True
        for element in self.edges:
            # print(element.dx.x,element.dx.y,element.dy.x,element.dy.y)
            lenx = (element.dx.x + element.dy.x) * blockWidth + blockWidth
            leny = (element.dx.y + element.dy.y) * blockWidth + blockWidth
            self.blocks.append(pygame.Rect(lenx, leny, blockWidth, blockWidth))
            self.dictor[node(lenx, leny)] = True
            # print(lenx,leny)
        # print('?')
        for element in self.blocks:
            self.parent.blit(image, element)
            #pygame.display.flip()
            pygame.display.update(pygame.Rect(element.x,element.y,blockWidth,blockWidth))
        return

    def drawMap(self, row=0, column=0):
        f = open("data.out", "w")
        self.drawEdge(row, column)
        #time.sleep(5)
        self.parent.fill(background_color)
        pygame.display.flip()

        rector = pygame.Rect(0, 0, blockWidth - 2, blockWidth - 2)

        for dy in range(0, 2 * column + 1):
            for dx in range(0, 2 * row + 1):
                rector.x = dx * blockWidth
                rector.y = dy * blockWidth
                # checker = True
                if node(rector.x, rector.y) not in self.dictor:
                    # if checker:
                    self.parent.blit(image, (rector.x, rector.y))
                    pygame.display.update(pygame.Rect(rector.x,rector.y,blockWidth,blockWidth))
                    f.write("1 ")
                else:
                    f.write("0 ")
            f.write("\n")
        f.close()
        character = pygame.image.load("endl.png").convert()
        character = pygame.transform.scale(character, (blockWidth, blockWidth))

        self.parent.blit(
            character,
            (
                self.srtx * 2 * blockWidth + blockWidth,
                self.srty * 2 * blockWidth + blockWidth,
            ),
        )
        # pygame.display.flip()
        pygame.display.update(
            pygame.Rect(
                self.srtx * 2 * blockWidth + blockWidth,
                self.srty * 2 * blockWidth + blockWidth,
                blockWidth,
                blockWidth,
            )
        )

        character = pygame.image.load("endl.png").convert()
        character = pygame.transform.scale(character, (blockWidth, blockWidth))
        self.parent.blit(
            character,
            (
                self.finx * 2 * blockWidth + blockWidth,
                self.finy * 2 * blockWidth + blockWidth,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                self.finx * 2 * blockWidth + blockWidth,
                self.finy * 2 * blockWidth + blockWidth,
                blockWidth,
                blockWidth,
            )
        )
