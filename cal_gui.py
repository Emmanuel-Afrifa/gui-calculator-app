import tkinter as tk
from tkinter import messagebox
import math
import sys

class Calc:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Basic Calculator')
        self.root.geometry('400x365')

        self.ent = tk.Entry(self.root)
        self.ent.bind('<KeyPress>',self.shortcut)
        self.ent.pack(fill='both',padx=10)

        self.buttframe = tk.Frame(self.root)
        self.buttframe.columnconfigure(0, weight=1)
        self.buttframe.columnconfigure(1, weight=1)
        self.buttframe.columnconfigure(2, weight=1)
        self.buttframe.columnconfigure(3, weight=1)


        #Creating the buttons
        self.butt7 = tk.Button(self.buttframe, text='7',padx=5,height=3, command=lambda: self.click(7))
        self.butt7.grid(column=0,row=2,sticky=tk.W +tk.E,pady=1)
        
        self.butt8 = tk.Button(self.buttframe, text='8',padx=5,height=3, command=lambda: self.click(8))
        self.butt8.grid(column=1,row=2,sticky=tk.W +tk.E,pady=1)
        self.butt9 = tk.Button(self.buttframe, text='9',padx=5,height=3, command=lambda: self.click(9))
        self.butt9.grid(column=2,row=2,sticky=tk.W +tk.E,pady=1)

        self.butt4 = tk.Button(self.buttframe, text='4',padx=5,height=3, command=lambda: self.click(4))
        self.butt4.grid(column=0,row=3,sticky=tk.W +tk.E,pady=1)
        self.butt5 = tk.Button(self.buttframe, text='5',padx=5,height=3, command=lambda: self.click(5))
        self.butt5.grid(column=1,row=3,sticky=tk.W +tk.E,pady=1)
        self.butt6 = tk.Button(self.buttframe, text='6',padx=5,height=3, command=lambda: self.click(6))
        self.butt6.grid(column=2,row=3,sticky=tk.W +tk.E,pady=1)

        self.butt1 = tk.Button(self.buttframe, text='1',padx=5,height=3, command=lambda: self.click(1))
        self.butt1.grid(column=0,row=4,sticky=tk.W +tk.E,pady=1)
        self.butt2 = tk.Button(self.buttframe, text='2',padx=5,height=3, command=lambda: self.click(2))
        self.butt2.grid(column=1,row=4,sticky=tk.W +tk.E,pady=1)
        self.butt3 = tk.Button(self.buttframe, text='3',padx=5,height=3, command=lambda: self.click(3))
        self.butt3.grid(column=2,row=4,sticky=tk.W +tk.E,pady=1)

        self.butt0 = tk.Button(self.buttframe, text='0',padx=5,height=3, command=lambda: self.click(0))
        self.butt0.grid(column=1,row=5,sticky=tk.W +tk.E,pady=1)
        
        self.buttadd = tk.Button(self.buttframe, text='+',padx=5,height=3, command=lambda: self.operation('add'))
        self.buttadd.grid(column=3,row=2,sticky=tk.W +tk.E,pady=1)

        self.buttsub = tk.Button(self.buttframe, text='-',padx=5,height=3, command=lambda: self.operation('sub'))
        self.buttsub.grid(column=3,row=3,sticky=tk.W +tk.E,pady=1)

        self.buttdiv = tk.Button(self.buttframe, text='/',padx=5,height=3, command=lambda: self.operation('div'))
        self.buttdiv.grid(column=3,row=4,sticky=tk.W +tk.E,pady=1)

        self.buttdot = tk.Button(self.buttframe, text='.',padx=5,height=3, command=self.decimal_point)
        self.buttdot.grid(column=2,row=5,sticky=tk.W +tk.E,pady=1)

        self.buttclear = tk.Button(self.buttframe, text='Clear', padx=5,height=3, command=self.clear_screen)
        self.buttclear.grid(column=0,row=0,sticky=tk.W +tk.E,pady=1)

        self.buttmod = tk.Button(self.buttframe, text='%',padx=5,height=3, command=lambda: self.operation('mod'))
        self.buttmod.grid(column=2,row=1,sticky=tk.W +tk.E,pady=1)

        self.buttdel = tk.Button(self.buttframe, text='<-', padx=5, height=3, command=self.delete)
        self.buttdel.grid(column=1,row=0,sticky=tk.W +tk.E,pady=1)

        
        self.buttmul = tk.Button(self.buttframe, text='x',padx=5,height=3, command=lambda: self.operation('mul'))
        self.buttmul.grid(column=3,row=1,sticky=tk.W +tk.E,pady=1)

        self.buttequal = tk.Button(self.buttframe, text='=', padx=5, height=3, command=self.results)
        self.buttequal.grid(column=3,row=5,columnspan=3,sticky=tk.W +tk.E,pady=1)

        self.buttnegate = tk.Button(self.buttframe, text='+/-', padx=5, height=3, command=self.negate)
        self.buttnegate.grid(column=0,row=5,sticky=tk.W +tk.E,pady=1)

        self.buttfact = tk.Button(self.buttframe, text='n!', padx=5, height=3, command=self.fact_func)
        self.buttfact.grid(column=0,row=1,sticky=tk.W +tk.E,pady=1)

        self.buttexponential = tk.Button(self.buttframe, text='e', padx=5, height=3, command=self.exponential)
        self.buttexponential.grid(column=1,row=1,sticky=tk.W +tk.E,pady=1) 

        self.buttinverse = tk.Button(self.buttframe, text='1/x', padx=5, height=3, command=self.inverse)
        self.buttinverse.grid(column=2,row=0,sticky=tk.W +tk.E,pady=1)

        self.buttpi = tk.Button(self.buttframe, text='pi', padx=5, height=3, command=self.func_pi)
        self.buttpi.grid(column=3,row=0,sticky=tk.W +tk.E,pady=1)


        self.buttframe.pack(fill='both')


        self.root.protocol('WM_DELETE_WINDOW', self.close)
        self.root.mainloop()

    def click(self,number):
        initial = self.ent.get()
        self.ent.delete(0, tk.END)
        self.ent.insert(0, str(initial) + str(number))

    def clear_screen(self):
        self.ent.delete(0,tk.END)

    def delete(self):
        initial = str(self.ent.get())
        new = initial[0:(len(initial)-1)]
        self.ent.delete(0,tk.END)
        self.ent.insert(0,new)

    def decimal_point(self):
        initial = str(self.ent.get())
        self.ent.delete(0,tk.END)
        self.ent.insert(0,initial+'.')

    def operation(self,param):
        global inn
        global key
        key = param
        initial = self.ent.get()
        self.ent.delete(0,tk.END)
        if '(' in initial: 
            if param == 'add':
                self.ent.insert(0,initial + ' + ')
            elif param == 'sub':
                self.ent.insert(0,initial + ' - ')
            elif param == 'mul':
                self.ent.insert(0,initial + ' x ')
            elif param == 'div':
                self.ent.insert(0,initial + ' / ')
            elif param == 'mod':
                self.ent.insert(0,initial + ' % ')
        else:      
            inn = float(initial)
            #self.ent.delete(0,tk.END)
       

    def results(self):
        actual_entry = self.ent.get() 
        if '(' in actual_entry:
            pass

        else:    
            try:
                new = float(self.ent.get())
            except:
                new = float(actual_entry[1:])
            self.ent.delete(0,tk.END)
            if key == 'add':
                answer = inn + new
            elif key == 'sub':
                answer = inn - new
            elif key == 'mul':
                answer = inn * new
            elif key == 'div':
                answer = inn / new
            elif key == 'mod':
                answer = inn % new
            elif key == '':
                answer = self.ent.get()
        
            self.ent.insert(0,str(answer))

            return answer 
    
    def negate(self):
        initial = self.ent.get()
        self.ent.delete(0,tk.END)
        if float(initial) > 0:
            self.ent.insert(0, '-'+initial)
        elif float(initial) < 0:
            self.ent.insert(0,initial[1:])

    def exponential(self):
        initial = self.ent.get()
        self.ent.delete(0,tk.END)
        self.ent.insert(0, str(math.e))

    # def openbracket(self):
    #     initial = self.ent.get()
    #     self.ent.delete(0,tk.END)
    #     new = initial + '('
    #     self.ent.insert(0,new)
    
    # def closebracket(self):
    #     initial = self.ent.get()
    #     self.ent.delete(0,tk.END)
    #     new = initial + ')'
    #     self.ent.insert(0,new)

    def factorial(self,num):
        if num == 0 or num == 1:
            return 1
        elif num > 1: 
            return num * self.factorial(num-1)
        
    def fact_func(self):
        initial = float(self.ent.get())
        self.ent.delete(0,tk.END)
        if initial < 0:
            self.ent.insert(0,'Invalid syntax')
        else:
            new = self.factorial(initial)
            self.ent.insert(0,str(new))

    
    def inverse(self):
        initial = float(self.ent.get())
        self.ent.delete(0,tk.END)
        new = 1/initial
        self.ent.insert(0,str(new))


    def func_pi(self):
        initial = self.ent.get()
        self.ent.delete(0,tk.END)
        new = math.pi
        self.ent.insert(0,str(new))
    

    def shortcut(self,event):
        if event.keysym == 'minus' and event.keycode == 189:
            # For some reason, 'add' is rather subtracts in response to the keypress.
            # Fix this!!!
            self.operation('add')
        elif event.keysym == 'slash' and event.keycode == 191:
            self.operation('div')
        elif event.keysym == 'asterisk' and event.keycode ==56:
            self.operation('mul')
        elif event.keysym == 'plus' and event.keycode == 187:
           # But this 'add' does exactly what it is supposed to do (Add the numbers).
            self.operation('add')
        elif event.keysym == 'percent' and event.keycode == 53:
               self.operation('mod')
        elif event.keysym == 'Delete' and event.keycode == 46:
            self.clear_screen()
        elif event.keysym == 'Return' and event.keycode == 13:
            self.results()
        # elif event.keysym == 'e' and event.keycode == 69:
        #     self.exponential()
        # print(event)


    # A function that asks for confirmation before closing the app.
    def close(self):
        if messagebox.askyesno(title='Close', message='Do you want to close the calculator?'):
            self.root.destroy()
        
c1 = Calc()
        