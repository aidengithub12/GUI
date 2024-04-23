import customtkinter as ctk
import tkinter as tk
import MasterFIle
import Calculate



ctk.set_appearance_mode("dark")
#window creation
window = ctk.CTk()
#set resolution
window.geometry('1920x1080')

class page1():
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
    Page2Button = ctk.CTkButton(window, text="Next Page", width=100,height=45,command=lambda: MasterFIle.toPage(page2()))
    #place buttons
    GTbutton.place(relx=0.064,rely=0.82685)
    WBbutton.place(relx = 0.1828125 , rely = 0.82685)
    ATbutton.place(relx=0.399791667 , rely = 0.82685)
    IRTbutton.place(relx = 0.52083 ,rely = 0.82685)
    Pbutton.place(relx = 0.2864593 ,rely = 0.82685)
    RHbutton.place(relx = 0.625 ,rely = 0.82685)
    WSbutton.place(relx = 0.0515625, rely = 0.2421875)
    WDbutton.place(relx = 0.0515625, rely = 0.1682291667)
    LATbutton.place(relx = 0.872916667, rely = 0.2421875)
    LONGbutton.place(relx = 0.872916667, rely = 0.1682291667)
    COMPbutton.place(relx=0.5,rely=0.5,anchor=tk.CENTER) #need to find place for
    Page2Button.place(relx=0.2,rely=0.2,anchor=tk.CENTER)
    # MasterFIle.getLiveGraph(Calculate.getSensorData()[1],Calculate.getSensorData()[2],window)
    def key_press():
        Calculate.changeCSV()
        print("Ran this code")

    #main loop
    window.bind('<Return>', key_press())
    window.update()
    window.mainloop()
tk.Frame(page1())