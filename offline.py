import sys
from function import *

print(sys.argv)
if(len(sys.argv)!=2):
    print("pas de ficher entré")
    exit()

#readline
try:
    path = sys.argv[1]
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
        if(int(tmp[0]) == 0 and cpt>0): 
            numTrame += 1
            tab.append([])
            cpt = 0
        if(int(tmp[0]) != cpt): 
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

        cpt += 10
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

print(tab)
fp.close()
for trame in tab:
    Ethernet(trame.copy())

root = tk.Tk()
root.mainloop()

