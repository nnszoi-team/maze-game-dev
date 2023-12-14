from collections.abc import Callable, Iterable, Mapping
import threading
from typing import Any
import pygame, signal
from maze import Maze
import interact, user

class RenderMovementThread(threading.Thread):
	def __init__(self, maze: Maze, blockWidth: int, screen: pygame.Surface, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
		super().__init__(group, target, name, args, kwargs, daemon=daemon)
		self.maze = maze
		self.blockWidth = blockWidth
		self.screen = screen

	def run(self):
		pass