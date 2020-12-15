import sys
from function import *
from gui import *

def openFile():
    fp = ""
    while 1==1:
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
    notify("Error","Too many arguements, choose a file instead")
    fp = openFile()
else:
    fp = open(sys.argv[1], 'r')

numTrame = 0
tab = [[]]
brut = [""]

while 1==1:
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
    break

#affichage
tramelist = []
titlelist = []
f = open("output.txt","w")
for trame in tab:
    try:
        out,title = Ethernet(trame.copy())
    except Exception:
        notify("Error","Error while analysing data")
        exit()

    tramelist.append(out)
    titlelist.append(title)
    f.write(out)
try:
    show(tramelist,titlelist,brut)
except Exception:
    notify("Error","Error while showing")
    exit()

f.close()
notify("Success","Info saved to output.txt")