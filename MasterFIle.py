import pandas as pd
import matplotlib.pyplot as plot
import matplotlib.animation as an
from matplotlib import style as st
import tkinter as tk
import Calculate
# i = int(0)
CSVhasChanged = False
def getGraph(xvalues, yvalues, var = "GT"):
    plot.plot(xvalues,yvalues)
    plot.xlabel('Time')
    plot.ylabel(str(var))
    plot.title(str(var) + " Vs. Time")
    plot.show()
#new_lst = sorted(lst, key=lambda x: x if isinstance(x, datetime) else datetime(x.year, x.month, x.day))
def sortTimes(times):
    # create dataframe
    df = pd.DataFrame({'name': times, 'count': len(times)}).sort_values('count', ascending=False)
    return times
def getLiveGraphTest1(xvalues,yvalues,self):
    import matplotlib
    matplotlib.use("TkAgg")
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.backends.backend_tkagg as mt
    from matplotlib.figure import Figure

    f = Figure(figsize=(1,1), dpi=100)
    a = f.add_subplot(111)
    a.plot(xvalues,yvalues)
    canvas = FigureCanvasTkAgg(f, self)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    toolbar = mt._backend_tk.NavigationToolbar2Tk(canvas, self)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
def getLiveGraphTest2():
    st.use("ggplot")
def printNew():
    global i
    i += 1
    print(i)
def getNewData():
    CSVhasChanged = True
    if (Calculate.csv == Calculate.MAINCSV):
        Calculate.csv = Calculate.TESTCSV
    else:
        Calculate.csv = Calculate.MAINCSV