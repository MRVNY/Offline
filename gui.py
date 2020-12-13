import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as st 
import os

def openFile():
    root = tk.Tk()
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("txt files","*.txt"),("all files","*.*")))
    return filename

def openWindow():
    root = tk.Tk()
    #canvas = tk.Canvas(root, height=700, width=700)
    #canvas.pack()
    #root.mainloop()
    return root

def addTrame(root, out):
    text_area = st.ScrolledText(root, width = 50, height = 10, font = ("Times New Roman", 15)) 
    text_area.grid(column = 0, pady = 10, padx = 10) 
  
    # Inserting Text which is read only 
    text_area.insert(tk.INSERT,out) 
    #l = tk.Label(root, text = out)
    #l.pack()

def show(root):
    root.mainloop()

