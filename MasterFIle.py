import Calculate
import matplotlib.pyplot as plot
def getGraph():
    data = Calculate.getSensorData()
    plot.plot(sorted(data[1]),data[2])
    plot.xlabel('Xaxis')
    plot.ylabel('Yaxis')
    plot.table('sensor data')
    plot.show()