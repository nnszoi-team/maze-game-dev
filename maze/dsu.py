class Dsu:
    def __init__(self, elementSize: int):
        self.__father_or_size = [1] * elementSize
        pass

    def get(self, currentElement: int) -> int:
        if self.__father_or_size[currentElement] <= 0:
            self.__father_or_size[currentElement] = -self.get(
                -self.__father_or_size[currentElement]
            )
            return -self.__father_or_size[currentElement]
        else:
            return currentElement

    def merge(self, elementA: int, elementB: int) -> bool:
        if self.same(elementA, elementB):
            return False
        elementA, elementB = self.get(elementA), self.get(elementB)
        sizeA, sizeB = self.__father_or_size[elementA], self.__father_or_size[elementB]
        if sizeA > sizeB:
            sizeA, sizeB = sizeB, sizeA
            elementA, elementB = elementB, elementA
        self.__father_or_size[elementB] += self.__father_or_size[elementA]
        self.__father_or_size[elementA] = -elementB
        return True

    def same(self, elementA: int, elementB: int) -> bool:
        return self.get(elementA) == self.get(elementB)
