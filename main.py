from maze import *
from graphix import *
import pygame, multiprocessing
import user, interactor, importlib
from constants import *

maze = Maze(30, 30, 0)
screenWidth = 0
screenHeight = 0
blockWidth = 10
screenHeight = max(screenHeight, maze.rowNumber * blockWidth) + 30
screenWidth = max(screenWidth, maze.columnNumber * blockWidth)
caption = "Maze Visualizer"

pygame.init()
screen = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption(caption, icontitle = caption)

visualizeMaze(maze, blockWidth, screen)

running = True

while running:
	pygame.time.Clock().tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				importlib.reload(user)
				print("Start running user's function to solve a maze")
				userInteractor = interactor.Interactor(maze, "pipe.txt")
				userProcess = multiprocessing.Process(target = user.main, args = [userInteractor])
				userProcess.daemon = True
				userProcess.start()
				userProcess.join(timeout = TIMEOUT_SECONDS)
				if userProcess.is_alive():
					userProcess.kill()
					userProcess.join()
					print("Timeout!")
				else:
					print("normal")

pygame.quit()
