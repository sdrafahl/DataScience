from __init__ import *
#visualizer = VisualizingData('green', 'o', 'solid')
#years = [1950, 1960 ,1970 ,1980 , 1990, 2000]
#gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.6]
#visualizer.displayPlotGraph(years, gdp, 'GDP Graph', 'Billions')
#visualizer.displayBarGraph(years, gdp, 'GDP Graph', 'Billions')
#testValues = [10, 10, 10, 30, 30]
#visualizer.displayDistributationGraph(testValues ,10 , "years", "GDP", "billions")
print "Vector Demo"

#vector = Vector()
#vector.addElement(5)
#vector.addElement(9)
#vector.addElement(8)
#vector.addElement(7)

print "Vector 1"
#vector.printVector()

#vector2 = Vector()
#vector2.addElement(10)
#vector2.addElement(9)
#vector2.addElement(82)
#vector2.addElement(0)

print "Vector 2"
#vector2.printVector()

print "Vector 3 = Vector 2 + Vector 1"
#vector3 = vector.addVector(vector2)

#vector3.printVector()

print "Vector Sum of Vector 1, Vector 2, Vector 3"

#vectors = [vector, vector2, vector3]

#vector4 = vectorSum(vectors)
#vector4.printVector()

print "Scalar Multiply Vector 4"

#vector4.scalarMultiply(10)
#vector4.printVector()

print "Vector Mean"

#vector5 = vectorMean(vectors)

#vector5.printVector()

print "Dot Product"

#print dotProduct(vector, vector2)

print "Standard Deviation Test"

stats = Statistics([4.52, 4.66, 4.66, 4.66, 4.66, 4.67, 4.67, 4.67, 4.67, 4.67,
 4.67, 4.67, 4.68, 4.68, 4.68, 4.68, 4.68, 4.68, 4.69, 4.69, 4.69, 4.69, 4.69, 4.69,
 4.69, 4.69, 4.69, 4.69, 4.69, 4.69, 4.69, 4.69, 4.70, 4.70, 4.70, 4.70, 4.70, 4.70,
 4.70, 4.70, 4.70, 4.71, 4.71, 4.71, 4.71, 4.72, 4.72, 4.72, 4.71])
print stats.standardDeviation()
