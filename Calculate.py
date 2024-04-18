# import pysensors
#wbgt
#heat index
import pandas as pd
import matplotlib as mp
csv = str("C:\\Users\\aiden\\OneDrive\\Documents\\Github\\python-sensor-gui\\Grandpa Project\\Variable_File.csv")
def getSensorData():
    data = pd.read_csv(csv)
    vars = [data.DATE,data.TIME,data.GT,data.WB,data.AT,data.IRT,data.P,data.RH,data.WS,data.WD,data.LAT,
    data.LON,data.COMP]
    with open("LOGFILE_VARS","w") as f:
        for i in range(0,len(vars)):
            f.write(str(vars[i]) + "\n")
    return vars
def changeCSV(csv = csv):
    csv = str("C:\\Users\\aiden\\OneDrive\\Documents\\Github\\python-sensor-gui\\Grandpa Project\\TestCSV.csv")
def CalcWBGT(vars):
    return (0.7 * vars[3][0]) + (0.2 * vars[2][0]) + (0.1 * vars[4][0])
def CalcHeatIndex():
    pass