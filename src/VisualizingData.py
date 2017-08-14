from matplotlib import pyplot as plt

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
