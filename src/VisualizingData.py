from matplotlib import pyplot as plt
from collections import Counter

class VisualizingData:

    def __init__(self, color, marker, linestyle):
        self.color = color
        self.marker = marker
        self.linestyle = linestyle

    def displayPlotGraph(self, xCoords, yCoords, title, ylabel):
        plt.plot(xCoords, yCoords, color = self.color, marker = self.marker, linestyle = self.linestyle)
        plt.title(title)
        plt.ylabel(ylabel)
        plt.show()

    def displayBarGraph(self, xCoords, yCoords, title, ylabel):
        xs = [i + 0.1 for i, _ in enumerate(xCoords)]
        plt.bar(xs, yCoords)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks([i + 0.5 for i, _ in enumerate(xCoords)], xCoords)
        plt.show()

    def displayDistributationGraph(self, values, rangeOfX, xlabel, ylabel, title):
        decile = lambda lamb: lamb // 10 * 10
        histogram = Counter(decile(lamb) for lamb in values)
        plt.bar([x - 4 for x in histogram.keys()], histogram.values(), 8)
        plt.axis([-5, 105, 0, 5])
        plt.xticks([10 * i for i in range(rangeOfX + 1)])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
