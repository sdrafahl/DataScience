from __init__ import *
#visualizer = VisualizingData('green', 'o', 'solid')
#years = [1950, 1960 ,1970 ,1980 , 1990, 2000]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.6]
#visualizer.displayPlotGraph(years, gdp, 'GDP Graph', 'Billions')
#visualizer.displayBarGraph(years, gdp, 'GDP Graph', 'Billions')
#testValues = [10, 10, 10, 30, 30]
#visualizer.displayDistributationGraph(testValues ,10 , "years", "GDP", "billions")

statistics = Statistics(gdp)
print statistics.valueOfQuantile(.5)
