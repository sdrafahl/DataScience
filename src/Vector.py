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

    def substractVector(self, vector):
        if len(self.array) == len(vector.array):
            newVector = Vector()
            counter = 0
            while counter < len(self.array):
                newVector.array.append(self.array[counter] - vector.array[counter])
                counter = counter + 1
            return newVector
        else:
            return -1

    def scalarMultiply(self, scalar):
        count = 0
        while count < len(self.array):
            self.array[count] = self.array[count] * scalar
            count = count + 1


    def vectorSum(vectors):
        newVector = Vector()
        counter = 0
        while counter < len(vectors[0].array):
                newVector.addElement(0)
                counter = counter + 1
        for vector in vectors:
            newVector = newVector.addVector(vector)
            if(newVector == -1):
                return -1
        return newVector

    def dotProduct(vector1, vector2):
        product = 0
        count = 0
        if len(vector1.array) == len(vector2.array):
            while count < len(vector1.array):
                product = product + vector1.array[count] * vector2.array[count]
                count = count + 1
            return product
        else:
            return -1

    def vectorMean(vectors):
        length = len(vectors)
        newVector = vectorSum(vectors)
        newVector.scalarMultiply(1.0/length)
        return newVector
