import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import tkinter.scrolledtext as st

root = tk.Tk()

frame1 = tk.Frame(root)
canvas1=tk.Canvas(frame1,height=400,width=550,scrollregion=(0,0,1300,1300))
analyser = canvas1.create_text(10, 10, anchor="nw")

frame2 = tk.Frame(root)
canvas2=tk.Canvas(frame2,height=200,width=550,scrollregion=(0,0,800,800))
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
    canvas1.grid()
    #y
    scrolly1 = tk.Scrollbar(frame1, orient="vertical", command=canvas1.yview)
    scrolly1.grid(row=0, column=1, sticky="ns")
    canvas1.configure(yscrollcommand=scrolly1.set)
    #x
    scrollx = tk.Scrollbar(frame1, orient="horizontal", command=canvas1.xview)
    scrollx.grid(row=1, column=0, sticky="we")
    canvas1.configure(xscrollcommand=scrollx.set)

    frame2.grid()
    canvas2.grid()
    #y
    scrolly2 = tk.Scrollbar(frame2, orient="vertical", command=canvas2.yview)
    scrolly2.grid(row=0, column=1, sticky="ns")
    canvas2.configure(yscrollcommand=scrolly2.set)

    root.mainloop()

def notify(s):
    tk.messagebox.showinfo('Success','Info saved to '+s)
