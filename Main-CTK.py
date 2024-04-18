import customtkinter as ctk
import tkinter as tk
import MasterFIle
import Calculate



ctk.set_appearance_mode("dark")
#window creation
window = ctk.CTk()
window.geometry('1080 * 1920')

#buttons
testbutton = ctk.CTkButton(window,text="test",command=MasterFIle.getGraph(x=Calculate.getSensorData()[0],y=Calculate.getSensorData()[2]))
testbutton.place(relx = 0.5,rely=0.6,anchor=tk.CENTER)


window.mainloop()