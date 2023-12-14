from collections.abc import Callable, Iterable, Mapping
from typing import Any
from maze import Maze
import threading
import random
import pygame

def visualize(maze: Maze, blockWidth: int, screen: pygame.Surface):
	block = []

	for i in range(maze.rowNumber):
		for j in range(maze.columnNumber):
			if maze.map[i][j] == '#':
				block.append(((255, 255, 255), pygame.Rect(i * blockWidth, j * blockWidth, blockWidth, blockWidth)))
			elif maze.map[i][j] == 'S':
				block.append(((255, 0, 0), pygame.Rect(i * blockWidth, j * blockWidth, blockWidth, blockWidth)))
			elif maze.map[i][j] == 'T':
				block.append(((0, 255, 0), pygame.Rect(i * blockWidth, j * blockWidth, blockWidth, blockWidth)))

	random.shuffle(block)

	for i in block:
		try:
			screen.fill(i[0], i[1])
		except pygame.error:
			break
	pygame.display.flip()

	pass


