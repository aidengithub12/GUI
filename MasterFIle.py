import pandas as pd
import matplotlib.pyplot as plot
def getGraph(xvalues, yvalues, var = "GT"):
    plot.plot(sorted(xvalues),yvalues)
    plot.xlabel('Time')
    plot.ylabel(str(var))
    plot.title(str(var) + " Vs. Time")
    plot.show()
#new_lst = sorted(lst, key=lambda x: x if isinstance(x, datetime) else datetime(x.year, x.month, x.day))
def sortTimes(times):
    # create dataframe
    df = pd.DataFrame({'name': times, 'count': len(times)}).sort_values('count', ascending=False)
    return times
