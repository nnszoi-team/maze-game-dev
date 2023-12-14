import interact
from reloading import reloading

@reloading
def another():
	print("what!")

@reloading
def main(M: interact.InteractMaze):
	print("main()))")
	while True:
		another()
		M.moveLeft()
		M.moveRight()
		M.moveUp()
		M.moveDown()
	print("okokokko")