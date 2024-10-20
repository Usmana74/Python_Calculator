from tkinter import Tk, Entry, Button, StringVar,PhotoImage


class Calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="black")
        master.resizable(False,False)
        
        self.logo = PhotoImage(file='apple.png')
        master.iconphoto(False,self.logo)
        
        self.equation=StringVar()
        self.entry_value=''
        self.result_shown = False
        Entry(width=17, bg='black', font=('Arial Bold',28),fg="white", textvariable=self.equation,justify="right").place(x=0,y=0,width=357,height=200)
        

        
        Button(width=11,height=3,text= '(',relief= 'raised',fg="white",bg='grey',command=lambda:self.show('(')).place(x=0,y=120)
        Button(width=11,height=3,text= ')',relief= 'raised',fg="white",bg='grey',command=lambda:self.show(')')).place(x=90,y=120)
        Button(width=11,height=3,text= 'del',relief= 'raised',fg="white",bg='grey',command=lambda:self.backspace()).place(x=180,y=120)
        Button(width=11,height=3,text= '1',relief= 'raised',fg="white",bg='Black',command=lambda:self.show('1')).place(x=0,y=180)
        Button(width=11,height=3,text= '2',relief= 'raised',fg="white",bg='Black',command=lambda:self.show('2')).place(x=90,y=180) 
        Button(width=11,height=3,text= '3',relief= 'raised',fg="white",bg='Black',command=lambda:self.show('3')).place(x=180,y=180)
        Button(width=11,height=3,text= '4',relief= 'raised',fg="white",bg='Black',command=lambda:self.show('4')).place(x=0,y=240)
        Button(width=11,height=3,text= '5',relief= 'raised',fg="white",bg='Black',command=lambda:self.show('5')).place(x=90,y=240)
        Button(width=11,height=3,text= '6',relief= 'raised',fg="white",bg='Black',command=lambda:self.show('6')).place(x=180,y=240)
        Button(width=11,height=3,text= '7',relief= 'raised',fg="white",bg='Black',command=lambda:self.show('7')).place(x=0,y=300)
        Button(width=11,height=3,text= '8',relief= 'raised',fg="white",bg='Black',command=lambda:self.show('8')).place(x=180,y=300)
        Button(width=11,height=3,text= '9',relief= 'raised',fg="white",bg='Black',command=lambda:self.show('9')).place(x=90,y=300)
        Button(width=11,height=3,text= '0',relief= 'raised',fg="white",bg='Black',command=lambda:self.show('0')).place(x=90,y=360)
        Button(width=11,height=3,text= '.',relief= 'raised',fg="white",bg='Black',command=lambda:self.show('.')).place(x=180,y=360)
        Button(width=11,height=3,text= '+',relief= 'raised',fg="white",bg='orange',command=lambda:self.show('+')).place(x=270,y=300)
        Button(width=11,height=3,text= '-',relief= 'raised',fg="white",bg='orange',command=lambda:self.show('-')).place(x=270,y=240)
        Button(width=11,height=3,text= '/',relief= 'raised',fg="white",bg='orange',command=lambda:self.show('/')).place(x=270,y=120)
        Button(width=11,height=3,text= 'X',relief= 'raised',fg="white",bg='orange',command=lambda:self.show('*')).place(x=270,y=180)
        Button(width=11,height=3,text= '=',relief= 'raised',fg="white",bg='orange',command=self.solve).place(x=270,y=360)
        Button(width=11,height=3,text= 'C',relief= 'raised',fg="white",bg="Black",command=self.clear).place(x=0,y=360)
        
    def show(self,value):
        if self.result_shown and value not in '+-*/':
            self.entry_value= ''
            
        self.result_shown = False
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)
        
        
    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)
        self.result_shown = False
        
    def solve(self):
        try:
           result = eval(self.entry_value)
           self.equation.set(result) 
           self.entry_value = str(result)
           self.result_shown = True
        except Exception as e:
            self.equation.set("error")
            self.entry_value = ''
            self.result_shown = False 
    
    def backspace(self):
        if not self.result_shown:
           self.entry_value = self.entry_value[:-1] 
           self.equation.set(self.entry_value)


root = Tk()
Calculator=Calculator(root)
root.mainloop()
