




import tkinter as tk



window = tk.Tk()
window.title( 'My Window')
window.geometry('400x400')

var1 = tk.StringVar()
var2 = tk.StringVar()
 


def print_selection():
    pass


lab = tk.Label(window,bg = 'yellow',textvariable = var1 ,width = 4, height = 2)
lab.pack()

b1 = tk.Button(window,text = "Print Selection",width = 15, height = 2,command = print_selection)
b1.pack()


var2.set((11,22,33,44,55,66,77,88,99,00))
lst = tk.Listbox(window,listvariable = var2)
lst.pack()


with open('text.txt','r') as fp:
    data = fp.readline()
    while data:
        lst.insert('end',data)
        data = fp.readline()




















window.mainloop()
