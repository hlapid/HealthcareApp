from FrontEnd.views import *
from Communication.model_input import Insert2DB
from Communication.model_query import DataQueries
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
        self.PatientIDEntry.bind("<Leave>", lambda e: app.inputs.set_val(self.PatientIDEntry,"PatientID"))
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
        self.PatientFirstNameEntry.bind("<Leave>", lambda e: app.inputs.set_val(self.PatientFirstNameEntry,'PatientFirstName'))

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
        self.PatientLastNameEntry.bind("<Leave>", lambda e: app.inputs.set_val(self.PatientLastNameEntry,'PatientLastName'))
        self.errorMassage = tk.Label(self,text="",fg="red",width=50,height=2)
        self.errorMassage.grid(column=2, row=2, columnspan = 5,padx=0, pady=0)

    def ID_error(self):
        self.errorMassage = tk.Label(self,text="ID error - numbers only please",
                                     fg="red",width=50,height=2)
        self.errorMassage.grid(column=1, row=2 , columnspan = 3, padx=5, pady=1)
        self.after(2000, self.errorMassage.destroy)
        return
    def clear_ID_error(self):
        self.errorMassage.destroy()
        return



class Frame2(ttk.Frame):
    def __init__(self,app):
        super().__init__(master=app,relief=tk.RAISED,borderwidth=5,width=200,height=10)
        self.__create_widgets(app)
        return
    def __create_widgets(self,app):
        self.labelDiagnosis = tk.Label(self,
                          text="Enter Diagnosis",
                          fg="black",  # Set the text color to white
                          bg="grey",  # Set the background color to black
                          width=13,
                          height=1)
        self.labelDiagnosis.pack(side=tk.LEFT)

        self.diag = tk.Text(self,width = 25,height =3)
        self.diag.pack(side=tk.LEFT)
        self.diag.bind("<Leave>", lambda e: app.inputs.set_val(self.diag, "Diagnosis"))

        self.rb_yes_var = tk.IntVar()
        self.rb_yes_var.set(0)
        self.rb_yes = tk.Radiobutton(self, text="Yes", variable=self.rb_yes_var, value=1,
                                     command=lambda : app.inputs.set_val(self.rb_yes_var,"DrugSensitivity"))
        self.rb_yes.pack(side=tk.LEFT)

        self.rb_no = tk.Radiobutton(self, text="No", variable=self.rb_yes_var, value=0,
                                     command=lambda : app.inputs.set_val(self.rb_yes_var,"DrugSensitivity"))
        self.rb_no.pack(side=tk.LEFT)

        self.labelCombo = tk.Label(master=self,
                          text="Antigen",
                          fg="black",  # Set the text color to white
                          bg="grey",  # Set the background color to black
                          width=8,
                          height=1)
        self.labelCombo.pack(side=tk.LEFT)
        self.comboAnt = ttk.Combobox(self,values=["Ant1", "Ant2","Ant3","Ant4"])
        self.comboAnt.pack(side=tk.LEFT)
        self.comboAnt.bind("<<ComboboxSelected>>", lambda e: app.inputs.set_val(self.comboAnt, "Antigen"))
        return True

class Frame4(ttk.Frame):
    def __init__(self,app):
        ttk.Frame.__init__(self,master=app,relief=tk.RAISED,borderwidth=2,width=120,height=60)
        self.createButton(app)
    def createButton(self,app):
        self.button = tk.Button(master=self,
                   text="Save&Exit",
                   bg="light green",
                   fg="black",
                   font=('Times New Roman',12),
                   command = lambda : app.inputs.controlButton())
        self.button.pack(side=tk.BOTTOM)
        return

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
        self.inputs = Insert2DB(self)
        self.__create_frames()
    def __create_frames(self):
        self.frame1 = Frame1(self)
        self.frame1.grid(column=1, row=1, padx=5, pady=1)
        self.frame2 = Frame2(self)
        self.frame2.grid(column=1, row=2, padx=5, pady=1)
        self.frame4 = Frame4(self)
        self.frame4.grid(column=1, row=4, padx=5, pady=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()


