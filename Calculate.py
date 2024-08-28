# import pysensors
#wbgt
#heat index
import pandas as pd
import matplotlib as mp
csv = str("C:\\Users\\aiden\\Documents\\GitHub\\GUI\\Variable_File.csv")#path for csv changes based off of computer
def getSensorData():
    data = pd.read_csv(csv)
    vars = [data.DATE,data.TIME,data.GT,data.WB,data.AT,data.IRT,data.P,data.RH,data.WS,data.WD,data.LAT,
    data.LON,data.COMP] #all data of csv
    with open("LOGFILE_VARS","w") as f:
        for i in range(0,len(vars)):
            f.write(str(vars[i]) + "\n")
    print("Ran with file: " + csv)
    return vars
def changeCSV(): #function to grab and change csv file - can be done externally though for extra performance
    global csv
    csv = str("C:\\Users\\aiden\\Documents\\GitHub\\GUI\\TestCSV.csv")
    print("CSV CHANGED")
def CalcWBGT(vars):
    return (0.7 * vars[3][0]) + (0.2 * vars[2][0]) + (0.1 * vars[4][0])
def CalcHeatIndex():
    pass