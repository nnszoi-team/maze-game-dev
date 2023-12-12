from maze import *
M = Maze(10, 10, 50)
for i in M.map:
    for j in i:
        print(j, end = '')
    print()
M.visualize(800, 600)