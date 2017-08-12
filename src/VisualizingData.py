from matplotlib import pyplot as plt

class VisualizingData:

    def __init__(self, color, marker, linestyle):
        self.color = color
        self.marker = marker
        self.linestyle = linestyle

    def displayPlotGraph(self, xCoords, yCoords, title, ylable):
        plt.plot(xCoords, yCoords, color = self.color, marker = self.marker, linestyle = self.linestyle)
        plt.title(title)
        plt.ylabel(ylable)
        plt.show()
