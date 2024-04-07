import Calculate
import matplotlib.pyplot as plot
def getGraph(xvalues, yvalues, var = "GT"):
    plot.plot(sorted(xvalues),yvalues)
    plot.xlabel('Time')
    plot.ylabel(str(var))
    plot.title(str(var) + " Vs. Time")
    plot.show()