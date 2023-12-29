import pygame
import time
import sys
import cgitb

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

from main import Background
from maze import Maze
from constants import *
from visualizer import Visualizer

cgitb.enable(format("text"))

userCodeLocate = "user.py"
locator = "user.py"
DfsSolution = "RightHandRuleSolution.py"
BfsSolution = "BfsSolution.py"
ShowWay = "DijkstraSolution.py"
randomMap = True

currentMaze = Maze(20, 20)


def executeCode(codeLocate: str):
    global Main, currentMaze

    pygame.init()
    if randomMap:
        currentMaze = Maze(20, 20)

    currentMaze.exportMazeMatrix()
    currentMaze.exportMazeGraph()

    Main = Background(currentMaze, CHARACTER_MOVE_SLEEP_TIME)
    Main.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    mazeVisualizer = Visualizer(Main.screen, currentMaze)
    mazeVisualizer.visualizeMazeMatrix()
    mazeVisualizer.visualizeCharacter(currentMaze.startingPoint)
    mazeVisualizer.visualizeCharacter(currentMaze.endPoint)

    time.sleep(EXECUTE_CODE_SLEEP_TIME)

    dictor = {
        "moveUp": Main.moveUp,
        "moveDown": Main.moveDown,
        "moveLeft": Main.moveLeft,
        "moveRight": Main.moveRight,
        "move": Main.move,
        "seekUp": Main.seekUp,
        "seekDown": Main.seekDown,
        "seekLeft": Main.seekLeft,
        "seekRight": Main.seekRight,
        "seek": Main.seek,
        "spawnNewCharacter": Main.spawnNewCharacter,
        "rowNumber": Main.rowNumber,
        "columnNumber": Main.columnNumber,
        "startingPoint": Main.startingPoint,
        "endPoint": Main.endPoint,
        "at": Main.at,
    }

    codeContent = open(codeLocate, encoding="utf-8", errors="ignore").read()

    try:
        exec(codeContent, dictor)
    finally:
        solutionAccepted = False
        for i in range(len(Main.characters)):
            if Main.characters[i].coordinate == currentMaze.endPoint:
                Main.run(Main.characters[i])
                solutionAccepted = True
                break
        if solutionAccepted == False:
            Main.run(Main.characters[0])


def executeUserCode():
    return executeCode("user.py")


def executeDfsSolutionCode():
    return executeCode("RightHandRuleSolution.py")


def executeBfsSolutionCode():
    return executeCode("BfsSolution.py")


def executeDijkstraSolutionCode():
    return executeCode("DijkstraSolution.py")


def turnMapRandom():
    global randomMap
    randomMap = not randomMap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumHeight(150)
        self.setMinimumWidth(250)
        self.setWindowTitle("Demo Runner")
        icon = QIcon("icon.png")

        self.setWindowIcon(icon)
        self.started = QPushButton("运行", self)
        self.started.setGeometry(0, 0, 125, 50)
        self.started.clicked.connect(lambda: executeUserCode())

        self.cleared = QPushButton("关闭窗口", self)
        self.cleared.setGeometry(125, 0, 125, 50)
        self.cleared.clicked.connect(lambda: pygame.quit())

        self.started = QPushButton("DFS 标程", self)
        self.started.setGeometry(0, 50, 125, 50)
        self.started.clicked.connect(lambda: executeDfsSolutionCode())

        self.cleared = QPushButton("BFS 标程", self)
        self.cleared.setGeometry(125, 50, 125, 50)
        self.cleared.clicked.connect(lambda: executeBfsSolutionCode())

        self.cleared = QPushButton("绘制最短道路", self)
        self.cleared.setGeometry(0, 100, 125, 50)
        self.cleared.clicked.connect(lambda: executeDijkstraSolutionCode())

        self.cleared = QPushButton("开关地图刷新", self)
        self.cleared.setGeometry(125, 100, 125, 50)
        self.cleared.clicked.connect(lambda: turnMapRandom())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    demo.show()
    sys.exit(app.exec_())
