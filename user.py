from interactor import *
from reloading import reloading

@reloading
def main(M: Interactor):
	print("main()))")
	for _ in range(1):
		print("down")
		M.move("down")
		print("up")
		M.move("up")
		M.move("left")
		M.move("right")
	print("okokokko")