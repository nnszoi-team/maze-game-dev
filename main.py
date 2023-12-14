from maze import Maze
import pygame
import random
import threading
import graphix.visualize as visualize
import graphix.movement as movement
import signal
import user
import interact
import multiprocessing
import time
from reloading import reloading

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

visualize.visualize(maze, blockWidth, screen)

running = True
TIMEOUT_SECONDS = 2

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				print("Start running user's function to solve a maze")
				userProcess = multiprocessing.Process(target = user.main, args = [interact.InteractMaze(maze, open("pipe.txt", "w"))])
				userProcess.daemon = True
				userProcess.start()
				userProcess.join(timeout = TIMEOUT_SECONDS)
				if userProcess.is_alive():
					userProcess.kill()
					userProcess.join()
					print("Timeout!")
				else:
					print("normal")
					pass

pygame.quit()
