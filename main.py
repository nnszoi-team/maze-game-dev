from maze import Maze
import pygame
import random
import threading
import visualize

maze = Maze(20, 20, 0)
screenWidth = 640
screenHeight = 480
blockWidth = 10
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

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False



pygame.quit()
