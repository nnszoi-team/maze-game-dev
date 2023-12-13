from maze import Maze
import pygame
import random
import threading
import visualize
import movement
import signal
import user
import interact
import multiprocessing
import time

maze = Maze(50, 50, 0)
screenWidth = 0
screenHeight = 0
blockWidth = 5
screenHeight = max(screenHeight, maze.rowNumber * blockWidth)
screenWidth = max(screenWidth, maze.columnNumber * blockWidth)
caption = "Maze Visualizer"

pygame.init()
screen = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption(caption, icontitle = caption)

renderMapThread = visualize.RenderMapThread(maze, blockWidth, screen)
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	if not renderMapThread.is_alive():
		try:
			renderMapThread.start()
		except:
			break

TIMEOUT_SECONDS = 1

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				print("fuck")
				print("22")
				process = multiprocessing.Process(target = user.main(interact.InteractMaze(maze, open("pipe.txt", "w"))))
				process.join(TIMEOUT_SECONDS)
				print("11")
				print("letsee")
				if process.is_alive():
					print("Timeout")
					process.terminate()
					process.join()
				else:
					print('end')

				# renderMovementThread = movement.RenderMovementThread(maze, blockWidth, screen)
				# renderMovementThread.start()

pygame.quit()
