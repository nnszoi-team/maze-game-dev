import pygame, sys
import time

from constants import BLOCK_WIDTH, BACKGROUND_COLOR, SHORTEST_PATH_SLEEP_TIME
from maze import Maze


class Character:
    def __init__(self, parent, maze: Maze):
        self.parent = parent
        self.coordinate = maze.startingPoint
        self.__maze = maze

    def __move_by_vector(self, vector: [int, int], cleared=True):
        if (
            self.coordinate[0] + vector[0] < 0
            or self.coordinate[0] + vector[0] >= self.__maze.rowNumber
        ):
            return self.parent.demoQuit()
        if (
            self.coordinate[1] + vector[1] < 0
            or self.coordinate[1] + vector[1] >= self.__maze.columnNumber
        ):
            return self.parent.demoQuit()
        if (
            self.__maze.matrix[self.coordinate[0] + vector[0]][
                self.coordinate[1] + vector[1]
            ]
            == 1
        ):
            return self.parent.demoQuit()

        newImage = pygame.image.load("character.png").convert()
        newImage = pygame.transform.scale(newImage, (BLOCK_WIDTH, BLOCK_WIDTH))

        if cleared == True:
            self.parent.screen.fill(
                BACKGROUND_COLOR,
                pygame.Rect(
                    self.coordinate[1] * BLOCK_WIDTH,
                    self.coordinate[0] * BLOCK_WIDTH,
                    BLOCK_WIDTH,
                    BLOCK_WIDTH,
                ),
            )
            pygame.display.update(
                pygame.Rect(
                    self.coordinate[1] * BLOCK_WIDTH,
                    self.coordinate[0] * BLOCK_WIDTH,
                    BLOCK_WIDTH,
                    BLOCK_WIDTH,
                )
            )
        if self.parent.prev[self.coordinate[0] + vector[0]][
            self.coordinate[1] + vector[1]
        ] == [0, 0]:
            self.parent.prev[self.coordinate[0] + vector[0]][
                self.coordinate[1] + vector[1]
            ] = self.coordinate

        self.coordinate[0] += vector[0]
        self.coordinate[1] += vector[1]

        self.parent.screen.blit(
            newImage,
            (
                self.coordinate[1] * BLOCK_WIDTH,
                self.coordinate[0] * BLOCK_WIDTH,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                self.coordinate[1] * BLOCK_WIDTH,
                self.coordinate[0] * BLOCK_WIDTH,
                BLOCK_WIDTH,
                BLOCK_WIDTH,
            )
        )
        time.sleep(self.parent.moveInterval)
        if pygame.event.peek(pygame.QUIT):
            pygame.quit()
            sys.exit()

    def moveUp(self, cleared=True):
        return self.__move_by_vector([-1, 0], cleared)

    def moveDown(self, cleared=True):
        return self.__move_by_vector([1, 0], cleared)

    def moveLeft(self, cleared=True):
        return self.__move_by_vector([0, -1], cleared)

    def moveRight(self, cleared=True):
        return self.__move_by_vector([0, 1], cleared)

    def move(self, direction: str, cleared=True):
        if direction == "Up":
            return self.moveUp(cleared)
        if direction == "Down":
            return self.moveDown(cleared)
        if direction == "Left":
            return self.moveLeft(cleared)
        if direction == "Right":
            return self.moveRight(cleared)
        return self.parent.demoQuit()

    def __seek_by_vector(self, vector: [int, int]):
        if (
            self.coordinate[0] + vector[0] < 0
            or self.coordinate[0] + vector[0] >= self.__maze.rowNumber
        ):
            return self.parent.demoQuit()
        if (
            self.coordinate[1] + vector[1] < 0
            or self.coordinate[1] + vector[1] >= self.__maze.columnNumber
        ):
            return self.parent.demoQuit()
        return self.__maze.matrix[self.coordinate[0] + vector[0]][
            self.coordinate[1] + vector[1]
        ]

    def seekUp(self):
        return self.__seek_by_vector([-1, 0])

    def seekDown(self):
        return self.__seek_by_vector([1, 0])

    def seekLeft(self):
        return self.__seek_by_vector([0, -1])

    def seekRight(self):
        return self.__seek_by_vector([0, 1])

    def seek(self, direction: str):
        print(f"seek {direction}")
        if direction == "Up":
            return self.seekUp()
        if direction == "Down":
            return self.seekDown()
        if direction == "Left":
            return self.seekLeft()
        if direction == "Right":
            return self.seekRight()
        return self.parent.demoQuit()


class Background:
    def __init__(self, maze: Maze, moveInterval: float):
        self.__maze = maze
        self.moveInterval = moveInterval
        self.prev = [
            [[0, 0] for _ in range(maze.columnNumber)] for _ in range(maze.rowNumber)
        ]
        self.startingPointXCoordinate = maze.startingPoint[0]
        self.startingPointYCoordinate = maze.startingPoint[1]
        self.characters = [Character(self, maze)]

    def drawPoint(self, coordinate: [int, int]):
        newImage = pygame.image.load("endl.png").convert()
        newImage = pygame.transform.scale(newImage, (BLOCK_WIDTH, BLOCK_WIDTH))
        self.screen.blit(
            newImage,
            (
                coordinate[1] * BLOCK_WIDTH,
                coordinate[0] * BLOCK_WIDTH,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                coordinate[1] * BLOCK_WIDTH,
                coordinate[0] * BLOCK_WIDTH,
                BLOCK_WIDTH,
                BLOCK_WIDTH,
            )
        )

    def drawShortestPath(self):
        newImage = pygame.image.load("endl.png").convert()
        newImage = pygame.transform.scale(newImage, (BLOCK_WIDTH, BLOCK_WIDTH))
        currentPoint = self.__maze.endPoint
        while currentPoint != self.__maze.startingPoint:
            self.screen.blit(
                newImage,
                (currentPoint[0] * BLOCK_WIDTH, currentPoint[1] * BLOCK_WIDTH),
            )
            pygame.display.update(
                pygame.Rect(
                    currentPoint[1] * BLOCK_WIDTH,
                    currentPoint[0] * BLOCK_WIDTH,
                    BLOCK_WIDTH,
                    BLOCK_WIDTH,
                )
            )
            time.sleep(SHORTEST_PATH_SLEEP_TIME)
            currentPoint = self.prev[currentPoint[0]][currentPoint[1]]
        self.screen.blit(
            newImage,
            (
                self.__maze.startingPoint[1] * BLOCK_WIDTH,
                self.__maze.startingPoint[0] * BLOCK_WIDTH,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                self.__maze.startingPoint[1] * BLOCK_WIDTH,
                self.__maze.startingPoint[0] * BLOCK_WIDTH,
                BLOCK_WIDTH,
                BLOCK_WIDTH,
            )
        )

    def demoQuit(self, textContent="Runtime Error"):
        font = pygame.font.Font("consola.ttf", 100)
        textSurface = font.render(textContent, True, (255, 221, 85))
        if textContent == "You Win!":
            self.drawShortestPath()
        self.screen.blit(textSurface, (50, 50))
        pygame.display.flip()
        running = True
        while running:
            if pygame.event.peek(pygame.QUIT):
                running = False
        pygame.quit()

    def moveUp(self, index=0, cleared=True):
        if index >= len(self.characters):
            return self.demoQuit()
        self.characters[index].moveUp(cleared)
        self.drawPoint([self.startingPointXCoordinate, self.startingPointYCoordinate])

    def moveDown(self, index=0, cleared=True):
        if index >= len(self.characters):
            return self.demoQuit()
        self.characters[index].moveDown(cleared)
        self.drawPoint([self.startingPointXCoordinate, self.startingPointYCoordinate])

    def moveLeft(self, index=0, cleared=True):
        if index >= len(self.characters):
            return self.demoQuit()
        self.characters[index].moveLeft(cleared)
        self.drawPoint([self.startingPointXCoordinate, self.startingPointYCoordinate])

    def moveRight(self, index=0, cleared=True):
        if index >= len(self.characters):
            return self.demoQuit()
        self.characters[index].moveRight(cleared)
        self.drawPoint([self.startingPointXCoordinate, self.startingPointYCoordinate])

    def move(self, index=0, direction: str = "", cleared=True):
        if index >= len(self.characters):
            return self.demoQuit()
        self.characters[index].move(direction, cleared)
        print(self.__maze.startingPoint)
        self.drawPoint([self.startingPointXCoordinate, self.startingPointYCoordinate])

    def seekUp(self, index=0):
        if index >= len(self.characters):
            return self.demoQuit()
        return self.characters[index].seekUp()

    def seekDown(self, index=0):
        if index >= len(self.characters):
            return self.demoQuit()
        return self.characters[index].seekDown()

    def seekLeft(self, index=0):
        if index >= len(self.characters):
            return self.demoQuit()
        return self.characters[index].seekLeft()

    def seekRight(self, index=0):
        if index >= len(self.characters):
            return self.demoQuit()
        return self.characters[index].seekRight()

    def seek(self, index=0, direction: str = ""):
        if index >= len(self.characters):
            return self.demoQuit()
        return self.characters[index].seek(direction)

    def run(self, checker: Character):
        if checker.coordinate != self.__maze.endPoint:
            return self.demoQuit("You Lose!")
        self.demoQuit("You Win!")

    def spawnNewCharacter(self, x: int, y: int):
        self.characters.append(Character(self, x, y))

    def rowNumber(self):
        return self.__maze.rowNumber

    def columnNumber(self):
        return self.__maze.columnNumber

    def startingPoint(self):
        return self.__maze.startingPoint

    def endPoint(self):
        return self.__maze.endPoint

    def at(self, coordinate: [int, int]):
        i, j = coordinate
        if i < 0 or i >= self.rowNumber:
            return self.demoQuit()
        if j < 0 or j >= self.columnNumber:
            return self.demoQuit()
        return self.__maze.matrix[i][j]
