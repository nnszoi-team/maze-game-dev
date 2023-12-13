import maze

class MazeInteract:
	def __init__(self, original: maze.Maze) -> None:
		self.__rowNumber = original.rowNumber
		self.__columnNumber = original.columnNumber
		self.__map = original.map
		self.__beginPoint = original.beginPoint
		self.__currentPoint = original.beginPoint
		self.__endPoint = original.endPoint
		self.__operation = []
		pass

	def seekOperation(self) -> []:
		return self.__operation

	def seekCoordinate(self, x: int, y: int) -> str:
		"""Return the state of the point at coordinate (x, y).
		
		'#' for wall, '.' for plain, and '-' for invalid queries (for example, out of range)
		"""
		if x < 0 or x >= self.__rowNumber or y < 0 or y >= self.__columnNumber:
			return "-"
		else:
			return self.__map[x][y]
		
	def seekCoordinate(self, coordinate: (int, int)) -> str:
		"""Return the state of the point at coordinate (x, y).
		
		'#' for wall, '.' for plain, and '-' for invalid queries (for example, out of range)
		"""
		x, y = coordinate[0], coordinate[1]
		return self.seekCoordinate(x, y)

	def currentPoint(self) -> (int, int):
		"""Return current point coordinate (x, y).
		"""
		return self.__currentPoint

	def beginPoint(self) -> (int, int):
		"""Return begin point coordinate (x, y).
		"""
		return self.__beginPoint
	
	def endPoint(self) -> (int, int):
		"""Return end point coordinate (x, y).
		"""
		return self.__endPoint

	def seekLeft(self) -> str:
		"""Return the state of the point to the left.
		
		'#' for wall, '.' for plain, and '-' for invalid queries (for example, out of range)
		"""	
		coordinate = list(self.currentPoint())
		coordinate[1] -= 1
		return self.seekCoordinate(tuple(coordinate))

	def seekRight(self) -> str:
		"""Return the state of the point to the right.
		
		'#' for wall, '.' for plain, and '-' for invalid queries (for example, out of range)
		"""
		coordinate = list(self.currentPoint())
		coordinate[1] += 1
		return self.seekCoordinate(tuple(coordinate))

	def seekUp(self) -> str:
		"""Return the state of the point to the up side.
		
		'#' for wall, '.' for plain, and '-' for invalid queries (for example, out of range)
		"""
		coordinate = list(self.currentPoint())
		coordinate[0] -= 1
		return self.seekCoordinate(tuple(coordinate))

	def seekDown(self) -> str:
		"""Return the state of the point to the down side.
		
		'#' for wall, '.' for plain, and '-' for invalid queries (for example, out of range)
		"""
		coordinate = list(self.currentPoint())
		coordinate[0] += 1
		return self.seekCoordinate(tuple(coordinate))

	def moveLeft(self) -> (bool, int, int):
		"""Move to the point to the left, and return a tuple of three elements.
		
		If the operation is valid, the first element is True, otherwise is False.
		
		The second and third element represent the coordinate of the new current point, remain the same when invalid.
		"""
		if self.seekLeft() == '#':
			return (False, self.currentPoint[0], self.currentPoint[1])
		else:
			self.__operation.append("left")
			self.currentPoint[1] -= 1
			return (True, self.currentPoint[0], self.currentPoint[1])

	def moveRight(self) -> (bool, int, int):
		"""Move to the point to the right, and return a tuple of three elements.
		
		If the operation is valid, the first element is True, otherwise is False.
		
		The second and third element represent the coordinate of the new current point, remain the same when invalid.
		"""
		if self.seekRight() == '#':
			return (False, self.currentPoint[0], self.currentPoint[1])
		else:
			self.__operation.append("right")
			self.currentPoint[1] += 1
			return (True, self.currentPoint[0], self.currentPoint[1])

	def moveUp(self) -> (bool, int, int):
		"""Move to the point to the up side, and return a tuple of three elements.
		
		If the operation is valid, the first element is True, otherwise is False.
		
		The second and third element represent the coordinate of the new current point, remain the same when invalid.
		"""
		if self.seekLeft() == '#':
			return (False, self.currentPoint[0], self.currentPoint[1])
		else:
			self.__operation.append("up")
			self.currentPoint[0] -= 1
			return (True, self.currentPoint[0], self.currentPoint[1])

	def moveDown(self) -> (bool, int, int):
		"""Move to the point to the down side, and return a tuple of three elements.

		If the operation is valid, the first element is True, otherwise is False.

		The second and third element represent the coordinate of the new current point, remain the same when invalid.
		"""
		if self.seekLeft() == '#':
			return (False, self.currentPoint[0], self.currentPoint[1])
		else:
			self.__operation.append("down")
			self.currentPoint[0] += 1
			return (True, self.currentPoint[0], self.currentPoint[1])

	def move(self, direction: str) -> (bool, int, int):
		"""Move to the point to the given direction, and return a tuple of three elements.

		The direction should be one of "left", "right", "up", "down", the case is not sensitive.

		If the operation is valid, the first element is True, otherwise is False.

		The second and third element represent the coordinate of the new current point, remain the same when invalid.
		"""
		if direction.lower() == "up":
			return self.moveUp()
		elif direction.lower() == "down":
			return self.moveDown()
		elif direction.lower() == "left":
			return self.moveLeft()
		elif direction.lower() == "right":
			return self.moveRight()
		else:
			return (False, self.currentPoint[0], self.currentPoint[1])
		