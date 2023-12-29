import random
from .dsu import Dsu


class Maze:
    def __init__(self, rowNumber: int, columnNumber: int) -> None:
        self.rowNumber = rowNumber
        self.columnNumber = columnNumber
        assert rowNumber >= 5 and columnNumber >= 5

        self.startingPoint = (0, 0)
        self.endPoint = (0, 0)
        while self.startingPoint == self.endPoint:
            self.startingPoint = (1, random.randint(1, columnNumber - 2))
            self.endPoint = (rowNumber - 2, random.randint(1, columnNumber - 2))

        edges = []
        for i in range(rowNumber):
            for j in range(columnNumber):
                current = (i, j)
                if i - 1 >= 0:
                    edges.append((current, (i - 1, j)))
                if i + 1 <= rowNumber - 1:
                    edges.append((current, (i + 1, j)))
                if j - 1 >= 0:
                    edges.append((current, (i, j - 1)))
                if j + 1 <= columnNumber - 1:
                    edges.append((current, (i, j + 1)))

        random.shuffle(edges)
        D = Dsu(rowNumber * columnNumber)
        temp = []
        for i in edges:
            u, v = i
            if D.same(u[0] * columnNumber + u[1], v[0] * columnNumber + v[1]):
                continue
            D.merge(u[0] * columnNumber + u[1], v[0] * columnNumber + v[1])
            temp.append(i)

        self.edges = []
        for i in temp:
            u, v = i
            middlePoint = (u[0] + v[0] + 1, u[1] + v[1] + 1)
            self.edges.append(((u[0] * 2 + 1, u[1] * 2 + 1), middlePoint))
            self.edges.append(((v[0] * 2 + 1, v[1] * 2 + 1), middlePoint))
        random.shuffle(self.edges)

        self.rowNumber = 2 * self.rowNumber + 1
        self.columnNumber = 2 * self.columnNumber + 1
        self.startingPoint = [
            self.startingPoint[0] * 2 + 1,
            self.startingPoint[1] * 2 + 1,
        ]
        self.endPoint = [self.endPoint[0] * 2 + 1, self.endPoint[1] * 2 + 1]
        self.matrix = [
            [1 for _ in range(self.columnNumber)] for _ in range(self.rowNumber)
        ]

        for i in self.edges:
            u, v = i
            self.matrix[u[0]][u[1]] = 0
            self.matrix[v[0]][v[1]] = 0

    def exportMazeGraph(self, fileName="maze_graph.txt"):
        fileObject = open(fileName, "w")
        fileObject.write(f"{self.rowNumber} {self.columnNumber} {len(self.edges)}\n")
        for i in self.edges:
            fileObject.write(f"{i[0][0]} {i[0][1]} {i[1][0]} {i[1][1]}\n")
        fileObject.close()

    def exportMazeMatrix(self, fileName="maze_matrix.txt"):
        fileObject = open(fileName, "w")
        fileObject.write(f"{self.rowNumber} {self.columnNumber}\n")
        fileObject.write(f"{self.startingPoint[0]} {self.startingPoint[1]}\n")
        fileObject.write(f"{self.endPoint[0]} {self.endPoint[1]}\n")
        for i in self.matrix:
            for j in i[:-1]:
                fileObject.write(f"{j} ")
            fileObject.write(f"{i[-1]}\n")
        fileObject.close()
