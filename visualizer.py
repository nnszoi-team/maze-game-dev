import pygame
from constants import BACKGROUND_COLOR, BLOCK_WIDTH
from maze import Maze

import time

image = pygame.image.load("block.png")
image = pygame.transform.scale(image, (BLOCK_WIDTH, BLOCK_WIDTH))


class Visualizer:
    def __init__(self, parent, maze: Maze):
        self.parent = parent
        self.__maze = maze

    def visualizeCharacter(self, pointCoordinate: [int, int]):
        character = pygame.image.load("endl.png").convert()
        character = pygame.transform.scale(character, (BLOCK_WIDTH, BLOCK_WIDTH))
        pointXCoordinate = pointCoordinate[0]
        pointYCoordinate = pointCoordinate[1]
        self.parent.blit(
            character,
            (
                pointYCoordinate * BLOCK_WIDTH,
                pointXCoordinate * BLOCK_WIDTH,
            ),
        )
        pygame.display.update(
            pygame.Rect(
                pointYCoordinate * BLOCK_WIDTH,
                pointXCoordinate * BLOCK_WIDTH,
                BLOCK_WIDTH,
                BLOCK_WIDTH,
            )
        )
        pass

    def visualizeMazeMatrix(self):
        self.parent.fill(BACKGROUND_COLOR)
        pygame.display.flip()

        rector = pygame.Rect(0, 0, BLOCK_WIDTH - 2, BLOCK_WIDTH - 2)

        for i in range(0, self.__maze.rowNumber):
            for j in range(0, self.__maze.columnNumber):
                rector.x = i * BLOCK_WIDTH
                rector.y = j * BLOCK_WIDTH
                if self.__maze.matrix[i][j] == 1:
                    self.parent.blit(image, (rector.y, rector.x))
                    pygame.display.update(
                        pygame.Rect(rector.y, rector.x, BLOCK_WIDTH, BLOCK_WIDTH)
                    )
