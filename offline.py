#readline

fp = open('echo-request.txt', 'r')

tab = []
line = fp.readline()
cpt = 0 #pour verifier offset 1

while line:
    tmp = line.split(" ")

    #verifier offset 1
    if(not int(tmp[0])==cpt): 
        print("error!")
    
    offset = tmp[0]
    del tmp[0:3]
    tmp[-1] = tmp[-1][0:2]

    #verifier offset 2
    if(int(offset,16) != len(tab)):
        print("offset error")
    tab += tmp

    line = fp.readline()
    cpt += 10

print(tab)

fp.close()