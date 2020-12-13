import tkinter as tk
import sys
from function import *
from gui import *

#print(sys.argv)
if(len(sys.argv)==1):
    path = openFile()
elif(len(sys.argv)>2):
    print("trop de arguments entrés")
    exit()
else:
    path = sys.argv[1]
#readline
try:
    fp = open(path, 'r')
except OSError:
    print("ficher error")
    exit()

numTrame = 0
tab = [[]]
line = fp.readline()
cpt = 0 #pour verifier offset 1

while line:
    if line != "\n":
        tmp = line.split(" ")

        #verifier offset 1
        if(int(tmp[0],16) == 0 and cpt>0): 
            numTrame += 1
            tab.append([])
            cpt = 0
        if(int(tmp[0],16) != cpt): 
            print("offset error")
            exit()

        offset = tmp[0]
        del tmp[0:3]
        tmp[-1] = tmp[-1][0:2]

        #verifier offset 2
        if(int(offset,16) != len(tab[numTrame])):
            print("offset error")
            exit()
        tab[numTrame] += tmp

        cpt += 16
    line = fp.readline()

#verifier format 
try:
    for oct in tab[numTrame]:
        if(len(oct)!=2 or int(oct,16)>255):
            print("format error")
            exit()
except ValueError:
    print("format error")
    exit()

#print(tab)
fp.close()

#affichage
#root = openWindow()
tramelist = []
titlelist = []
#f = open("output.txt","w")
for trame in tab:
    out,title = Ethernet(trame.copy())
    print(title)
    print(out+"\n")
    tramelist.append(out)
    titlelist.append(title)
    #f.write(out)

show(tramelist,titlelist)
#f.close()
#notify("output.txt")