import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import tkinter.scrolledtext as st

root = tk.Tk()
#label = tk.Label(root,justify=tk.LEFT)
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
canvas1=tk.Canvas(frame1,height=400,width=500,scrollregion=(0,0,1000,1000))
analyser = canvas1.create_text(10, 10, anchor="nw")
canvas2=tk.Canvas(frame2,height=200,width=500,scrollregion=(0,0,500,500))
raw = canvas2.create_text(10, 10, anchor="nw")



class Trame:

    def __init__(self,s,t,brut,i):

        self.title = str(i+1)+" - "+t
        self.s = s
        self.i = 0
        self.brut = brut

class Menu:

    def __init__(self):

        self.menu = tk.Listbox(root,width=60,height=5)
        self.menu.bind("<<ListboxSelect>>", self.click)
        self.tlist = []
        self.strlist = []
        self.blist = []

    def click(self,event):
        res = self.menu.curselection()
        i = res[0]
        s = self.strlist[i]
        b = self.blist[i]
        print(b)

        canvas1.itemconfig(analyser,text=s)
        canvas2.itemconfig(raw,text=b)

    
    def insert(self,tr):
        self.menu.insert(len(self.tlist),tr.title)
        self.strlist.append(tr.s)
        self.tlist.append(tr.title)
        self.blist.append(tr.brut)


def openFile():
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("txt files","*.txt"),("all files","*.*")))
    return filename

def show(trl,ttl,brut):
    m = Menu()
    for i in range(len(trl)):
        trame = Trame(trl[i],ttl[i],brut[i],i)
        m.insert(trame)
    m.menu.grid()
    frame1.grid()
    frame2.grid()
    canvas1.grid()
    canvas2.grid()
    scroll1 = tk.Scrollbar(frame1, orient="vertical", command=canvas1.yview)
    scroll1.grid(row=0, column=1, sticky="ns")
    canvas1.configure(yscrollcommand=scroll1.set)
    scroll2 = tk.Scrollbar(frame2, orient="vertical", command=canvas2.yview)
    scroll2.grid(row=0, column=1, sticky="ns")
    canvas2.configure(yscrollcommand=scroll2.set)
    root.mainloop()

def notify(s):
    tk.messagebox.showinfo('Success','Info saved to '+s)
