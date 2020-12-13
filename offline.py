import sys
import tkinter as tk
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
tab = [][]
line = fp.readline()
cpt = 0 #pour verifier offset 1

while line:
    tmp = line.split(" ")

    #verifier offset 1
    if(int(tmp[0]) != cpt): 
        print("offset error")
        exit()

    offset = tmp[0]
    del tmp[0:3]
    tmp[-1] = tmp[-1][0:2]

    #verifier offset 2
    if(int(offset,16) != len(tab)):
        print("offset error")
        exit()
    tab += tmp

    line = fp.readline()
    cpt += 10

#verifier format 
try:
    for oct in tab:
        if(len(oct)!=2 or int(oct,16)>255):
            print("format error")
            exit()
except ValueError:
    print("format error")
    exit()

print(tab)
fp.close()
Ethernet(tab.copy())



