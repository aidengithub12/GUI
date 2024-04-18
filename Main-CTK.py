import customtkinter as ctk
import tkinter as tk
import MasterFIle
import Calculate



ctk.set_appearance_mode("light")
#window creation
window = ctk.CTk()
#set resolution
window.geometry('1920x1080')


# testbutton = ctk.CTkButton(window,text="test",command= lambda: MasterFIle.getGraph(xvalues=Calculate.getSensorData()[0],yvalues=Calculate.getSensorData()[2]))
# testbutton.place(relx = 0.5,rely=0.6,anchor=tk.CENTER)

#All reading variables
GT = 0 #temp
WB = 0 #temp
AT = 0 #temp
IR = 0 #temp
BAR = 0 #float
RH = 0 #float
WD = 0 #int
WS = 0 #int
LAT = 0 #float
LONG = 0 #float
"""
x = 123, y = 893 #done
x = 351, y = 893 #done
x = 791, y = 893 #done
x = 1000, y = 893 #done
x = 550, y = 893 #done
x = 1200, y = 893 #done
x = 99, y = 465
x = 99, y = 323
x = 1100, y = 465
x = 1100, y = 323
"""
# #buttons
GTbutton = ctk.CTkButton(window,text="GT",command=lambda: MasterFIle.getGraph(xvalues=Calculate.getSensorData()[1],yvalues=Calculate.getSensorData()[2]))
WBbutton = ctk.CTkButton(window, text="WB", command=lambda: MasterFIle.getGraph(xvalues=Calculate.getSensorData()[1],yvalues=Calculate.getSensorData()[3],var="WB"))
ATbutton = ctk.CTkButton(window, text="AT", command=lambda: MasterFIle.getGraph(xvalues=Calculate.getSensorData()[1],yvalues=Calculate.getSensorData()[4],var="AT"))
IRTbutton = ctk.CTkButton(window, text="IRT", command=lambda: MasterFIle.getGraph(xvalues=Calculate.getSensorData()[1],yvalues=Calculate.getSensorData()[5],var="IRT"))
Pbutton = ctk.CTkButton(window, text="P", command=lambda: MasterFIle.getGraph(xvalues=Calculate.getSensorData()[1],yvalues=Calculate.getSensorData()[6],var="P"))
RHbutton = ctk.CTkButton(window, text="RH", command=lambda: MasterFIle.getGraph(xvalues=Calculate.getSensorData()[1],yvalues=Calculate.getSensorData()[7],var="RH"))
WSbutton = ctk.CTkButton(window, text="WS", command=lambda: MasterFIle.getGraph(xvalues=Calculate.getSensorData()[1],yvalues=Calculate.getSensorData()[8],var="WS"))
WDbutton = ctk.CTkButton(window, text="WD", command=lambda: MasterFIle.getGraph(xvalues=Calculate.getSensorData()[1],yvalues=Calculate.getSensorData()[9],var="WD"))
LATbutton = ctk.CTkButton(window, text="LAT", command=lambda: MasterFIle.getGraph(xvalues=Calculate.getSensorData()[1],yvalues=Calculate.getSensorData()[10],var="LAT"))
LONGbutton = ctk.CTkButton(window, text="LONG", command=lambda: MasterFIle.getGraph(xvalues=Calculate.getSensorData()[1],yvalues=Calculate.getSensorData()[11],var="LONG"))
COMPbutton = ctk.CTkButton(window, text="COMP", command=lambda: MasterFIle.getGraph(xvalues=Calculate.getSensorData()[1],yvalues=Calculate.getSensorData()[12],var="COMP"))

#place buttons
GTbutton.place(relx=0.064,rely=0.82685)
WBbutton.place(relx = 0.1828125 , rely = 0.82685)
ATbutton.place(relx=0.399791667 , rely = 0.82685)
IRTbutton.place(relx = 0.52083 ,rely = 0.82685)
Pbutton.place(relx = 0.2864593 ,rely = 0.82685)
RHbutton.place(relx = 0.625 ,rely = 0.82685)
WSbutton.place(relx = 0.0515625, rely = 0.2421875)
WDbutton.place(relx = 0.0515625, rely = 0.1682291667)
LATbutton.place(relx = 0.572916667, rely = 0.2421875)
LONGbutton.place(relx = 0.572916667, rely = 0.1682291667)
COMPbutton.place(relx=0.5,rely=0.5,anchor=tk.CENTER) #need to find place for

def key_press():
    Calculate.changeCSV()
    print("Ran this code")

#main loop
window.bind('<Return>', key_press())
window.mainloop()