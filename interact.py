import maze

class MazeInteract:
	def __init__(self, original: maze.Maze) -> None:
		self.__rowNumber = original.rowNumber
		self.__columnNumber = original.columnNumber
		self.__map = original.map
		self.__beginPoint = original.beginPoint
		self.__currentPoint = original.beginPoint
		self.__endPoint = original.endPoint
		pass

	import random
	random.randint()

	def seekCoordinate(self, x: int, y: int) -> str:
		"""Return the state of the point at coordinate (x, y).
		
		'#' for wall, and '.' for plain.
		"""
		pass

	def currentPoint(self) -> (int, int):
		"""Return current point coordinate (x, y).
		"""
		pass

	def beginPoint(self) -> (int, int):
		"""Return begin point coordinate (x, y).
		"""
		pass

	def endPoint(self) -> (int, int):
		"""Return end point coordinate (x, y).
		"""
		pass

	def seekLeft(self) -> str:
		"""Return the state of the point to the left.
		
		'#' for wall, and '.' for plain.
		"""
		pass

	def seekRight(self) -> str:
		"""Return the state of the point to the right.
		
		'#' for wall, and '.' for plain.
		"""
		pass

	def seekUp(self) -> str:
		"""Return the state of the point to the up side.
		
		'#' for wall, and '.' for plain.
		"""
		pass

	def seekDown(self) -> str:
		"""Return the state of the point to the down side.
		
		'#' for wall, and '.' for plain.
		"""
		pass

	def moveLeft(self) -> (bool, int, int):
		"""Move to the point to the left, and return a tuple of three elements.
		
		If the operation is valid, the first element is True, otherwise is False.
		
		The second and third element represent the coordinate of the new current point, remain the same when invalid.
		"""
		pass

	def moveRight(self) -> (int, int):
		"""Move to the point to the right, and return a tuple of three elements.
		
		If the operation is valid, the first element is True, otherwise is False.
		
		The second and third element represent the coordinate of the new current point, remain the same when invalid.
		"""
		pass

	def moveUp(self) -> (int, int):
		"""Move to the point to the up side, and return a tuple of three elements.
		
		If the operation is valid, the first element is True, otherwise is False.
		
		The second and third element represent the coordinate of the new current point, remain the same when invalid.
		"""
		pass

	def moveDown(self) -> (int, int):
		"""Move to the point to the down side, and return a tuple of three elements.

		If the operation is valid, the first element is True, otherwise is False.

		The second and third element represent the coordinate of the new current point, remain the same when invalid.
		"""
		pass