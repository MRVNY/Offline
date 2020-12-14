import tkinter as tk
import sys
from function import *
from gui import *

#print(sys.argv)
if(len(sys.argv)==1):
    path = openFile()
elif(len(sys.argv)>2):
    print("too many arguments")
    exit()
else:
    path = sys.argv[1]
#readline
try:
    fp = open(path, 'r')
except OSError:
    print("file error")
    exit()

numTrame = 0
tab = [[]]
brut = [""]

for line in fp.read().lower().splitlines():
    tmp = line.split(' ')

    #verifier offset
    offset = tmp.pop(0)
    try:
        if(int(offset,16) == 0 and len(tab[numTrame])>0): 
            numTrame += 1
            tab.append([])
            brut.append("")
        if(int(offset,16) != len(tab[numTrame])): 
            print("offset error")
            exit()
    except ValueError:
        continue

    brut[numTrame] += offset + "  "

    #verifier format / eliminer mots invalides
    
    for oct in tmp:
        try:
            if(len(oct)==2 and int(oct,16)<=255):
                brut[numTrame] += " " + oct
                tab[numTrame].append(oct)
        except ValueError:
            continue

    brut[numTrame] += "\n"

    line = fp.readline()



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
    #print(out+"\n")
    tramelist.append(out)
    titlelist.append(title)
    #f.write(out)

show(tramelist,titlelist,brut)
#f.close()
#notify("output.txt")