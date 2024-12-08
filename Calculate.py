# import pysensors
#wbgt
#heat index
import pandas as pd
import matplotlib as mp
MAINCSV = str("C:\\Users\\aiden\\Documents\\GitHub\\GUI\\Variable_File.csv")
TESTCSV = str("C:\\Users\\aiden\\Documents\\GitHub\\GUI\\TestCSV.csv")
csv = MAINCSV#path for csv changes based off of computer
isnew = False
def getSensorData():
    data = pd.read_csv(csv)
    vars = [data.DATE,data.TIME,data.GT,data.WB,data.AT,data.IRT,data.P,data.RH,data.WS,data.WD,data.LAT,
    data.LON,data.COMP] #all data of csv
    with open("LOGFILE_VARS","w") as f:
        for i in range(0,len(vars)):
            f.write(str(vars[i]) + "\n")
    print("Ran with file: " + csv)
    return vars

def CalcWBGT(vars):
    return (0.7 * vars[3][0]) + (0.2 * vars[2][0]) + (0.1 * vars[4][0])
def CalcHeatIndex():
    pass