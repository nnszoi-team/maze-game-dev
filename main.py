from maze import Maze
import pygame
import random
import threading

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

class RenderMapThread(threading.Thread):

	def run(self):

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

renderMapThread = RenderMapThread()
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
