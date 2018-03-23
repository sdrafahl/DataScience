class Statistics:

    def __init__(self):
        self.dataList = []

    def __init__(self, data):
        self.dataList = data

    def addData(self, value):
        self.dataList.append(value)

    def numberOfValues(self):
        return len(self.dataList)

    def mean(self):
        return sum(self.dataList) / len(self.dataList)

    def valueOfQuantile(self, quantile):
        index = (quantile * (len(self.dataList) - 1)) - 1
        rightDecimal = index - (int(index) + 0.0)
        leftDecimal = 1 - rightDecimal
        return self.dataList[int(index)] * leftDecimal + self.dataList[int(index) + 1] * rightDecimal
