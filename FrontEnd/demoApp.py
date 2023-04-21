import tkinter as tk
from tkinter import ttk
import sys
from screeninfo import get_monitors

class Frame1(ttk.Frame):
    def __init__(self,app):
        ttk.Frame.__init__(self,master=app,relief=tk.RAISED,borderwidth=2,width=500,height=30)
        self.__create_widgets(app)
        return
    def __create_widgets(self,app):
        self.columnconfigure([1,2,3,4,5,6], weight=1, minsize=10)
        self.rowconfigure([1,2], weight=1, minsize=20)

        # Patient ID label
        self.labelPatientID = tk.Label(self,
                 text="Patient ID",
                 fg="black",  # Set the text color to white
                 bg="grey",  # Set the background color to black
                 width=12,
                 height=1)
        self.labelPatientID.grid(column=1, row=1, padx=0, pady=1)
        # Patient ID Entry
        self.PatientIDEntry = tk.Entry(self,width = 22)
        self.PatientIDEntry.insert(0, "patient id")
        self.PatientIDEntry.grid(column=2, row=1, padx=0, pady=1)
        self.PatientIDEntry.bind("<Button-1>", lambda e: self.PatientIDEntry.delete(0, "end"))
        self.PatientIDEntry.bind("<Leave>", lambda e: print(f"{self.PatientIDEntry.get()}"))
        # Patient first name label
        self.labelPatientFirstName = tk.Label(self,
                 text="Patient's First Name",
                 fg="black",  # Set the text color to white
                 bg="grey",  # Set the background color to black
                 width=20,
                 height=1)
        self.labelPatientFirstName.grid(column=3, row=1, padx=1, pady=1)
        # self.labelPatientFirstName.pack(side=tk.LEFT)
        # Patient first name entry
        self.PatientFirstNameEntry = tk.Entry(self,width = 20)
        self.PatientFirstNameEntry.insert(0, "patient's first name")
        self.PatientFirstNameEntry.grid(column=4, row=1, padx=2, pady=1)
        # self.PatientFirstNameEntry.pack(side=tk.LEFT)
        self.PatientFirstNameEntry.bind("<Button-1>", lambda e: self.PatientFirstNameEntry.delete(0,"end"))
        self.PatientFirstNameEntry.bind("<Leave>", lambda e: print(self.PatientFirstNameEntry.get()))

        # Patient last name label
        self.labelPatientLastName = tk.Label(self,
                 text="Patient's Last Name",
                 fg="black",  # Set the text color to white
                 bg="grey",  # Set the background color to black
                 width=20,
                 height=1)
        self.labelPatientLastName.grid(column=5, row=1, padx=1, pady=1)
        # self.labelPatientLastName.pack(side=tk.LEFT)
        # Patient last name entry
        self.PatientLastNameEntry = tk.Entry(self,width = 20)
        self.PatientLastNameEntry.insert(0, "patient's last name")
        self.PatientLastNameEntry.grid(column=6, row=1, padx=0, pady=1)
        # self.PatientLastNameEntry.pack(side=tk.LEFT)
        self.PatientLastNameEntry.bind("<Button-1>", lambda e: self.PatientLastNameEntry.delete(0,"end"))
        self.PatientLastNameEntry.bind("<KeyRelease>", lambda e: print(self.PatientLastNameEntry.get()))
        self.errorMassage = tk.Label(self,text="",fg="red",width=50,height=2)
        self.errorMassage.grid(column=2, row=2, columnspan = 5,padx=0, pady=0)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Apointment Manager')
        self.width = get_monitors()[0].width
        self.height = get_monitors()[0].height
        self.geometry(f"{int(0.8*self.width):d}x{int(0.8*self.height):d}")
        self.resizable(True,True)
        self.columnconfigure([1], weight=1, minsize=10)
        self.rowconfigure([1,2,3,4], weight=1, minsize=120)
        self.__create_frames()
    def __create_frames(self):
        self.frame1 = Frame1(self)
        self.frame1.grid(column=1, row=1, padx=5, pady=1)
        pass
if __name__ == "__main__":
    app = App()
    app.mainloop()


