from collections.abc import Callable, Iterable, Mapping
from typing import Any
from maze import Maze
import threading
import user
import interact
import multiprocessing
import time

class UserFunctionThread(threading.Thread):
	def __init__(self, maze: Maze, pipeFileObject = open("pipe.txt", "w"), group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
		super().__init__(group, target, name, args, kwargs, daemon=daemon)
		self.maze = maze
		self.pipeFileObject = pipeFileObject

	def run(self):
		process = multiprocessing.Process(target = user.main(interact.InteractMaze(self.maze, self.pipeFileObject)))
		process.start()
		TIMEOUT = 0.1
		# process.join(TIMEOUT)
		time.sleep(TIMEOUT)
		print("letsee")

		if process.is_alive():
			print("Timeout")
			process.terminate()
			process.join()
		
		print('end')
