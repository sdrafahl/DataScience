class Statistics:

    def __init__(self):
        self.dataList = []

    def addData(self, value):
        self.dataList.append(value)

    def numberOfValues(self):
        return len(self.dataList)
