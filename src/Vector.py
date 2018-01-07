
class Vector:

    def __init__(self):
        self.array = []

    def printVector(self):
        print self.array

    def addElement(self, element):
        self.array.append(element)

    def removeElement(self, element):
        self.array.remove(element)

    def addVector(self ,vector):
        if len(self.array) == len(vector.array):
            newVector = Vector()
            counter = 0
            while counter < len(self.array):
                newVector.array.append(self.array[counter] + vector.array[counter])
                counter = counter + 1
            return newVector
        else:
            return -1
