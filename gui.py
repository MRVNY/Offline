import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox

root = tk.Tk()
label = tk.Label(root,justify=tk.LEFT)

class Trame:

    def __init__(self,s,t,i):

        self.title = str(i+1)+" - "+t
        self.s = s
        self.i = 0

class Menu:

    def __init__(self):

        self.menu = tk.Listbox(root,width=50,height=5)
        self.menu.bind("<<ListboxSelect>>", self.click)
        self.tlist = []
        self.strlist = []

    def click(self,event):
        label.pack()
        res = self.menu.curselection()
        i = res[0]
        s = self.strlist[i]
        label.config(text=s)
    
    def insert(self,tr):
        self.menu.insert(len(self.tlist),tr.title)
        self.strlist.append(tr.s)
        self.tlist.append(tr.title)


def openFile():
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("txt files","*.txt"),("all files","*.*")))
    return filename

def show(trl,ttl):
    m = Menu()
    for i in range(len(trl)):
        trame = Trame(trl[i],ttl[i],i)
        m.insert(trame)
    m.menu.pack()
    root.mainloop()

def notify(s):
    tk.messagebox.showinfo('Success','Info saved to '+s)
