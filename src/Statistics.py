import math

class Statistics:

    def __init__(self):
        self.dataList = []

    def __init__(self, data):
        self.dataList = data

    def addData(self, value):
        self.dataList.append(value)

    def numberOfValues(self):
        return len(self.dataList)

    def standardDeviation(self):
        n = self.numberOfValues()
        sampleMean = sum(self.dataList)/n
        sumValue = 0
        for x in self.dataList:
            sumValue += (x - sampleMean) ** 2
        return math.sqrt((sumValue / n))
