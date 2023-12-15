from maze import Maze
import random
import pygame

def visualizeMaze(maze: Maze, blockWidth: int, screen: pygame.Surface):
	"""Visualize the maze using pygame lib.
	"""
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


