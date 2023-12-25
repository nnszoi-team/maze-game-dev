import pygame
import time
import sys
import cgitb

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

from main import BackMap, character
from printMap import node, edge, background, image, blockWidth,screenHeight,screenWidth

cgitb.enable(format("text"))

#Main.init()
locator='user.py'
DfsSolution='RightHandRuleSolution.py'
BfsSolution='BfsSolution.py'

def started():
    global Main,locator
    pygame.init()
    Main = BackMap()
    Main.init()
    Main.screen = pygame.display.set_mode((screenWidth, screenHeight))
    backGround = background(
        Main.screen, Main.edges, Main.srtx, Main.srty, Main.finx, Main.finy
    )
    backGround.drawMap(Main.row, Main.column)
    #print(123123)
    dictor={
    'moveUp':Main.moveUp,
    'moveDown':Main.moveDown,
    'moveLeft':Main.moveLeft,
    'moveRight':Main.moveRight,
    'spawnNewCharacter':Main.spawnNewCharacter,
    'Main':Main
    }
    file_contents = open(locator,encoding='utf-8',errors='ignore').read()
    try:
        exec(file_contents,dictor)
    finally:
        for i in range(len(Main.characters)):
            if Main.characters[i].x==Main.finx and Main.characters[i].y==Main.finy:
                Main.run(Main.characters[i])
                break
    locator='user.py'

def setDfs():
    global locator,DfsSolution
    locator=DfsSolution
    
def setBfs():
    global locator,BfsSolution
    locator=BfsSolution

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        #self.setCentralWidget(self.view)
        self.setWindowTitle("Demo Runner")
        # 修改按钮和文本框位置请修改 setGeometry 内参数
        # setGeometry格式：前两个坐标表示其位置，后两个坐标表示其长度与宽度
        self.started = QPushButton('运行',self)
        self.started.setGeometry(0,0,125,50)
        self.started.clicked.connect(lambda:started())
        
        self.cleared = QPushButton('关闭窗口',self)
        self.cleared.setGeometry(125,0,125,50)
        self.cleared.clicked.connect(lambda:pygame.quit())
        
        self.started = QPushButton('DFS标程',self)
        self.started.setGeometry(0,50,125,50)
        self.started.clicked.connect(lambda:setDfs())
        
        self.cleared = QPushButton('BFS标程',self)
        self.cleared.setGeometry(125,50,125,50)
        self.cleared.clicked.connect(lambda:setBfs())
        
        #self.start.clicked.connect(lambda:self.clicked())
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    demo.show()
    sys.exit(app.exec_())
    