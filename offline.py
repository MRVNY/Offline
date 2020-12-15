import sys
from function import *
from gui import *

def openFile():
    fp = ""
    while True:
        try:
            fp = open(openPath(), 'r')
            break
        except OSError:
            if fp == "": exit()
            continue
    return fp

#verifier filepath
if(len(sys.argv)==1):
    fp = openFile()
elif(len(sys.argv)>2):
    notify("Error","Too many arguements, please select a file instead")
    fp = openFile()
else:
    try:
        fp = open(sys.argv[1], 'r')
    except FileNotFoundError:
        notify("Error","File not found, please select another file")
        fp = openFile()

numTrame = 0
tab = [[]]
brut = [""]

while True:
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
                notify("Error","Offset error, please select another file")
                fp.close()
                fp = openFile()
                break
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

    fp.close()

    #affichage
    ifBreak = True
    tramelist = []
    titlelist = []
    f = open("output.txt","w")
    for trame in tab:
        try:
            out,title = Ethernet(trame.copy())
        except Exception:
            notify("Error","Error while analysing data, please select another file")
            fp = openFile()
            ifBreak = False
            break

        tramelist.append(out)
        titlelist.append(title)
        f.write(out)

    if ifBreak:
        try:
            show(tramelist,titlelist,brut)
        except Exception:
            notify("Error","Error while showing, please select another file")
            fp = openFile()
            ifBreak = False
    
    f.close()
    if ifBreak: break

notify("Success","Info saved to output.txt")