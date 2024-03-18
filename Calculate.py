# import pysensors
#wbgt
#heat index
def getSensorData():
    fileContents = ""
    seperatedData = []
    lastCommaPosition = 0
    with open(('C:\\Users\\aiden\\OneDrive\\Documents\\GitHub\\python-sensor-gui\\Grandpa Project\\dataHolderClimate.csv'
           ),'r') as csvfile:
        fileContents = csvfile.read()
        csvfile.close()
    for i in range(len(fileContents)):
        if fileContents[i] == ',':
            seperatedData.append(fileContents[lastCommaPosition:(i)])
            lastCommaPosition = i + 1
    print(seperatedData)
    
def CalcWBGT(file):
    pass
def CalcHeatIndex():
    pass