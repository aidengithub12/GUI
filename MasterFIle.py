import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plot
import matplotlib.animation as an
from matplotlib import style as st


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
def getLiveGraph():
    st.use("ggplot")
    