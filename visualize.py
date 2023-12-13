from collections.abc import Callable, Iterable, Mapping
from typing import Any
from maze import Maze
import threading
import random
import pygame

class RenderMapThread(threading.Thread):
	def __init__(self, maze: Maze, blockWidth: int, screen: pygame.Surface, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
		super().__init__(group, target, name, args, kwargs, daemon=daemon)
		self.maze = maze
		self.blockWidth = blockWidth
		self.screen = screen

	def run(self):

		block = []

		for i in range(self.maze.rowNumber):
			for j in range(self.maze.columnNumber):
				if self.maze.map[i][j] == '#':
					block.append(((255, 255, 255), pygame.Rect(i * self.blockWidth, j * self.blockWidth, self.blockWidth, self.blockWidth)))
				elif self.maze.map[i][j] == 'S':
					block.append(((255, 0, 0), pygame.Rect(i * self.blockWidth, j * self.blockWidth, self.blockWidth, self.blockWidth)))
				elif self.maze.map[i][j] == 'T':
					block.append(((0, 255, 0), pygame.Rect(i * self.blockWidth, j * self.blockWidth, self.blockWidth, self.blockWidth)))

		random.shuffle(block)

		for i in block:
			try:
				self.screen.fill(i[0], i[1])
			except pygame.error:
				break
		pygame.display.flip()
