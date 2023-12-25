"""
一、
你可以直接调用以下函数用于调试你的程序：
moveUp(idx,True/False,True/False)用于使第idx个节点向上移动一步；
moveDown(idx,True/False,True/False)用于使第idx个节点向下移动一步；
moveLeft(idx,True/False,True/False)用于使第idx个节点向左移动一步；
moveRight(idx,True/False,True/False)用于使第idx个节点向右移动一步。
其中括号内第一个参数为节点下标，
第二个参数为是否更新节点（目前已经废弃），
第三个参数为是否清除原来的痕迹（即是否保留原有的痕迹）。
（第二、三个参数只会对迷宫的显示产生影响，均不对代码正确性产生影响！）
注：如果不传入参数，则会使用默认参数(0,True,True)

二、
如果想要访问每个节点的具体内容，请使用
Main.characters[idx].x,
Main.characters[idx].y 对其横纵坐标进行查询。

三、
如果想访问每条边的具体内容，请使用
Main.edges[idx].x,
Main.edges[idx].y 对其连接的两端（均为节点）进行查询。

四、
如果需要新增一个节点，请使用以下函数：
spawnNewCharacter(x,y)。
该函数将在点(x,y)位置处生成一个新节点。

五、
如果想访问关于背景相关的数据，请使用
Main.row 以获得迷宫的行数；
Main.column 以获得迷宫的列数；
Main.counts 以获得路径数；
Main.srtx 以获得起点横坐标；
Main.srty 以获得起点纵坐标；
Main.finx 以获得终点横坐标；
Main.finy 以获得终点纵坐标。
注：由于地图是会进行初始化刷新的，这些数据将会根据每次刷新的结果进行更新，即只能在运行时由程序获得。

六、
如果需要读入文件，请使用open函数
具体用法示例如下：
f = open("Maze.out", "r")
f.readline()
...
其中在文件中调用f.readline()等价于在控制台中调用input()。

七、
运行时只需要保存即可，
不需要在此处加入
if __name__=='__main__':
之类用于运行的函数。

以下为示例，若有任何问题请参考下发的 README.txt 文本文档。
"""


while True:
    moveRight()
    moveLeft()


