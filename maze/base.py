from .dsu import *
import random
import pygame

class Maze:
	def __init__(self, rowNumber: int, columnNumber: int, minimumEdgeNumber: int):
		D = Dsu(rowNumber * columnNumber)
		alternativeEdge = {(i, i + 1) for i in range(rowNumber * columnNumber) if i % columnNumber != columnNumber - 1} \
			| {(i, i + columnNumber) for i in range(rowNumber * columnNumber) if i // columnNumber != rowNumber - 1}
		beginPoint = random.randint(0, rowNumber * columnNumber - 1)
		endPoint = beginPoint
		while endPoint == beginPoint:
			endPoint = random.randint(0, rowNumber * columnNumber - 1)

		resultEdge = set()
		
		while minimumEdgeNumber > 0 or not D.same(beginPoint, endPoint):
			randomEdge = alternativeEdge.pop()
			if D.same(randomEdge[0], randomEdge[1]):
				alternativeEdge.add(randomEdge)
			else:
				resultEdge.add(randomEdge)
				D.merge(randomEdge[0], randomEdge[1])
				minimumEdgeNumber -= 1
		
		map = [['#'] * (2 * columnNumber + 1) for _ in range(2 * rowNumber + 1)]
		
		for x in range(rowNumber):
			for y in range(columnNumber):
				map[2 * x + 1][2 * y + 1] = '.'

		for p, q in resultEdge:
			pX = p // columnNumber
			pY = p % columnNumber
			qX = q // columnNumber
			if pX == qX:
				map[pX * 2 + 1][pY * 2 + 2] = '.'
			else:
				map[pX * 2 + 2][pY * 2 + 1] = '.'
				
		self.map = map
		self.columnNumber = 2 * columnNumber + 1
		self.rowNumber = 2 * rowNumber + 1
		self.beginPoint = ((beginPoint // columnNumber) * 2 + 1, (beginPoint % columnNumber) * 2 + 1)
		self.endPoint = ((endPoint // columnNumber) * 2 + 1, (endPoint % columnNumber) * 2 + 1)
			
	def visualize(self, screenWidth: int, screenHeight: int):
		pygame.init()
		screen = pygame.display.set_mode([640, 480])
		pygame.display.set_caption("Maze Visualizer", icontitle = "Maze Visualizer")

		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
		pygame.quit()