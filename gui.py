import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
label = tk.Label(root,justify=tk.LEFT)
buttonlist = []
def openFile():
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("txt files","*.txt"),("all files","*.*")))
    return filename

def show(l):
    for i in range(len(l)):
        trameButton = TrameButton(l[i],i)
        trameButton.button.pack()
    root.mainloop()

class TrameButton:

    def __init__(self,tr,i):

        self.tr = tr
        self.button = tk.Button(root,text="trame"+str(i),padx=200,command=self.click)

    def click(self):
        label.pack()
        label.config(text=self.tr)