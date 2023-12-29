row = 0
column = 0
counts = 0
srtx = 0
srty = 0
finx = 0
finy = 0
blocks = []
turn = "Down"


def readFile():
    global blocks
    global row, column, counts, srtx, srty, finx, finy
    f = open("Maze.out", "r")
    row, column = [int(i) for i in f.readline().split()]
    counts = int(f.readline())
    srtx, srty, finx, finy = [int(i) for i in f.readline().split()]
    f.close()
    f = open("data.out", "r")
    memory = []
    for j in range(2 * column + 1):
        line = [int(i) for i in f.readline().split()]
        memory.append(line)
        pass
    for j in range(2 * row + 1):
        line = []
        for i in range(2 * column + 1):
            line.append(memory[i][j])
        blocks.append(line)
    f.close()


def RightWay():
    global turn
    global blocks
    global row, column
    while Main.characters[0].x != finx or Main.characters[0].y != finy:
        dx = Main.characters[0].x
        dy = Main.characters[0].y
        if turn == "Left":
            if blocks[dx * 2 + 1][dy * 2] == 0 and dy != 0:
                Main.characters[0].moveUp()
                turn = "Up"
            elif blocks[dx * 2][dy * 2 + 1] == 0 and dx != 0:
                Main.characters[0].moveLeft()
                turn = "Left"
            else:
                turn = "Down"

        elif turn == "Right":
            if blocks[dx * 2 + 1][dy * 2 + 2] == 0 and dy != row - 1:
                moveDown()
                turn = "Down"
            elif blocks[dx * 2 + 2][dy * 2 + 1] == 0 and dx != row - 1:
                moveRight()
                turn = "Right"
            else:
                turn = "Up"

        elif turn == "Up":
            if blocks[dx * 2 + 2][dy * 2 + 1] == 0 and dx != row - 1:
                moveRight()
                turn = "Right"
            elif blocks[dx * 2 + 1][dy * 2] == 0 and dy != 0:
                moveUp()
                turn = "Up"
            else:
                turn = "Left"
        elif turn == "Down":
            if blocks[dx * 2][dy * 2 + 1] == 0 and dx != 0:
                moveLeft()
                turn = "Left"
            elif blocks[dx * 2 + 1][dy * 2 + 2] == 0 and dy != column - 1:
                moveDown()
                turn = "Down"
            else:
                turn = "Right"


readFile()
RightWay()
# Main.run(Main.characters[0])
