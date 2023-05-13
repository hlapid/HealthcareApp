from FrontEnd.views import *
from Communication.model_input import Insert2DB
from Communication.model_query import DataQueries

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Apointment Manager')
        self.geometry('1200x800')
        self.resizable(True,True)
        self.inputs = Insert2DB(self)
        self.queries = DataQueries(self,"emr")
        # layout on the root window
        self.Change_Frame(0)

    def Change_Frame(self, num):
        wig = self.grid_slaves()
        for l in wig:
            l.destroy()
        if num==0:
            self.frame0 = Frame0(self)
            self.frame0.grid(row=0,column = 0,padx=500,pady=250)
        elif num==1:
            self.frame1 = Frame1(self)
            self.frame1.grid(column=1, row=1, padx=200, pady=100)
            self.frame2= Frame2(self)
            self.frame2.grid(column=1, row=2, padx=200, pady=100)
            self.frame4= Frame4(self)
            self.frame4.grid(column=1, row=3, padx=200, pady=100)
        elif num==2:
            self.frame3= Frame3(self)
            self.frame3.grid(row=0,column = 0,padx=100,pady=250)

if __name__ == "__main__":
    app = App()
    app.mainloop()
