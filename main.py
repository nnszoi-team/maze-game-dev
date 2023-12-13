from maze import *
M = Maze(50, 50, 0)
for i in M.map:
    for j in i:
        print(j, end = '')
    print()
M.visualize(0, 0, 10)