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

while True:
    numTrame = 0
    tab = [[]]
    brut = [""]
    ifBreak = True
    for line in fp.read().lower().splitlines():
        tmp = line.split(' ')

        #verifier offset
        offset = tmp.pop(0)
        try:
            if(int(offset,16) == 0 and len(tab[numTrame])>0): 
                numTrame += 1
                tab.append([])
                brut.append("")
            if(int(offset,16) > len(tab[numTrame])): 
                notify("Error","Offset error, please select another file")
                fp.close()
                fp = openFile()
                ifBreak = False
                break
            brut[numTrame] = brut[numTrame][0:len(brut[numTrame])-3*(len(tab[numTrame])-int(offset,16))]
            brut[numTrame] += "\n"
            tab[numTrame] = tab[numTrame][0:int(offset,16)]
        except ValueError:
            continue

        #verifier format / eliminer mots invalides
        brut[numTrame] += offset + "  "
        for oct in tmp:
            try:
                if(len(oct)==2 and int(oct,16)<=255):
                    brut[numTrame] += " " + oct
                    tab[numTrame].append(oct)
            except ValueError:
                continue

    if ifBreak: fp.close()

    tramelist = []
    titlelist = []
    output = open("output.txt","w")

    #analyse & write
    if ifBreak: 
        for trame in tab:
            try:
                out,title = Ethernet(trame.copy())
            except IndexError:
                notify("Error","Erreur trame non complete à la ligne "+str(len(trame)//16+1)+" octet n° "+str(len(trame)%16+1))
                output.close()
                open("output.txt", 'w').close()
                fp = openFile()
                ifBreak = False
                break
            except Exception as text:
                notify("Error",repr(text))
                output.close()
                open("output.txt", 'w').close()
                fp = openFile()
                ifBreak = False
                break
            

            tramelist.append(out)
            titlelist.append(title)
            output.write("##########\n"+str(titlelist.index(title)+1)+" - "+title+"\n##########\n")
            output.write(out+"\n\n")

    #affichage
    if ifBreak:
        try:
            show(tramelist,titlelist,brut)
        except Exception:
            notify("Error","Error while showing, please select another file")
            output.close()
            open("output.txt", 'w').close()
            fp = openFile()
            ifBreak = False
            break
        output.close()
    
    if ifBreak: break

notify("Success","Info saved to output.txt")