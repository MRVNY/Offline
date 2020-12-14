def Ethernet(tab):
    out = "Couche Eternet : \n"
    out += "\tDestination address : "+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+"\n"
    out += "\tSource address : "+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+"\n"
    typeEternet = tab.pop(0)+tab.pop(0)
    if typeEternet == "0800":
        out += "\tEtherType : Ipv4 (0x0800)\n"
        out += "\tData : "+str(len(tab))+" octets \n"
        s,title = Ipv4(tab)
        out += s
    elif typeEternet == "0806":
        out += "\tEtherType : ARP (0x0806)\n"
        out += "\tData : "+str(len(tab))+" octets \n"
    else : 
        out += "\tEtherType : Non reconnu\n"
        out += "\tData : "+str(len(tab))+" octets \n"
    return out,title


def Ipv4(tab):
    out = "Couche Ip :\n"
    out += "\tVersion : Ipv4 (0x"+ tab[0][0]+")\n"
    headerLength = int(tab[0][1],16)*4
    out += "\tHeader Length : "+ str(headerLength) +" octets (0x"+tab.pop(0)[1]+")\n"
    out += "\tType of Service :"+ tab.pop(0) +"\n"
    t = int(tab[0]+tab[1],16)
    out += "\tTotal Length : "+ str(t)+ " octets (0x"+ tab.pop(0)+tab.pop(0)+")\n"
    out += "\tIdentifier : 0x"+ tab.pop(0)+tab.pop(0)+ "\n"
    out += "\tFlags : "
    f = bin(int(tab.pop(0), 16))[2:].zfill(8)
    out += "\tReserved : "+ f[0]+"\n"
    out += "\t\tDon't Fragment (DF) : "+ f[1]+ "\n"
    out += "\t\tMore Fragment (MF) : "+f[2]+"\n"
    g = bin(int(tab.pop(0), 16))[2:].zfill(8)
    h = f[3:]+g
    out += "\t\tFragment Offset : "+ str(int(h,2))+"(0b"+str(h)+")\n"
    out += "\tTime to live (TTL) : "+str(int(tab[0],16))+"(0x"+tab.pop(0)+")\n"
    proto = int(tab.pop(0),16)
    out += "\tProtocol : "
    if (proto == 1): 
        out += "\tICMP (0x01)\n"
        protoname = "ICMP"
    elif (proto == 6): 
        out += ("\tTCP (0x06)\n")
        protoname = "TCP"
    elif (proto == 17): 
        out += "\tUDP (0x11)\n"
        protoname = "UDP"
    else: 
        out += "\tNon reconnu\n"
        protoname = "Unknown"
    out += "\tHeader Checksum : 0x"+ tab.pop(0)+tab.pop(0)+"\n"
    ipsrc = str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))
    out += "\tSource Ip Adress : "+ipsrc+"\n"
    ipdst = str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))
    out += "\tDestination Ip Adress : "+ipdst+"\n"
    title = "Src: "+ipsrc+" Dst: "+ipdst+" Protocol: "+protoname
    #option
    optnumber = 1
    optTotalLength = headerLength -20
    while (optTotalLength > 0):
        out += "Option n° "+optnumber+ "\n Type : "
        opt = tab.pop(0)
        if (opt == "00"): 
            out += "End of Options List\n"
            optTotalLength-=1
        elif (opt =="01"):
            out += "No Operation\n"
            optTotalLength-=1
        elif (opt == "07"):
            out += "Record Route\n"
            optLength = tab.pop(0)
            optTotalLength -=int(optLength,16)
            out += "Length : " + int(optLength,16) +" (Ox"+ optLength+ ")\n"
            out += "Pointer : "+ tab.pop(0)+"\n"
            optLength = int(optLength,16)-3
            routerNo = 1
            while(optLength != 0):
                out += "Router n°"+str(routerNo)+" : "+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16)) +"\n"
                optLength-=1
                routerNo+=1
        elif (opt == "44"):
            out += "Time Stamp\n"
            optLength = tab.pop(0)
            optTotalLength -=int(optLength,16)
            out += "Length : " + int(optLength,16) +" (Ox"+ optLength+ ")\n"
            out += "Pointer : "+ tab.pop(0)+"\n"
            optLength = int(optLength,16)-3
            while(optLength !=0) : 
                tab.pop(0)
                optLength +=1
        elif (opt == "83"):
            out += "Loose Routing\n"
            optLength = tab.pop(0)
            optTotalLength -=int(optLength,16)
            out += "Length : " + int(optLength,16) +" (Ox"+ optLength+ ")\n"
            out += "Pointer : "+ tab.pop(0)+"\n"
            optLength = int(optLength,16)-3
            while(optLength !=0) : 
                tab.pop(0)
                optLength +=1
        elif (opt == "89"):
            out += "Strict Routing\n"
            optLength = tab.pop(0)
            optTotalLength -=int(optLength,16)
            out += "Length : " + int(optLength,16) +" (Ox"+ optLength+ ")\n"
            out += "Pointer : "+ tab.pop(0)+"\n"
            optLength = int(optLength,16)-3
            while(optLength !=0) : 
                tab.pop(0)
                optLength +=1
        else :
            out += "Non Reconnu\n"
            optLength = tab.pop(0)
            optTotalLength -=int(optLength,16)
            out += "Length : " + int(optLength,16) +" (Ox"+ optLength+ ")\n"
            out += "Pointer : "+ tab.pop(0)+"\n"
            optLength = int(optLength,16)-3
            while(optLength !=0) : 
                tab.pop(0)
                optLength +=1
        optnumber +=1
    out += "\tData : "+str(len(tab))+" octets \n"
    if (proto ==6): out+= tcp(tab)
    return out,title

def tcp(tab):
    out = "Couche tcp \n"
    scrport = int(tab.pop(0)+tab.pop(0),16)
    out += "\tSource port number : "+ str(scrport)+"\n"
    dstport = int(tab.pop(0)+tab.pop(0),16)
    out += "\tDestination port number : "+ str(dstport)+"\n"
    out += "\tSequence number : "+ tab.pop(0)+tab.pop(0)+tab.pop(0)+tab.pop(0)+"\n"
    out += "\tAcknowledgement number : "+ tab.pop(0)+tab.pop(0)+tab.pop(0)+tab.pop(0)+"\n"
    headerLength = int(tab[0][0],16)*4
    out += "\tHeader Length : "+ str(headerLength) +" octets ("+tab[0][0]+")\n"
    f = bin(int(tab.pop(0)[1]+tab.pop(0), 16))[2:].zfill(12)
    out += "\tFlags : \n"
    out += "\t\tNS : "+ f[3]
    out += "\n\t\tCWR : "+ f[4]
    out += "\n\t\tECE : "+ f[5]
    out += "\n\t\tURG : "+ f[6]
    out += "\n\t\tACK : "+ f[7]
    out += "\n\t\tPSH : "+ f[8]
    out += "\n\t\tRST : "+ f[9]
    out += "\n\t\tSYN : "+ f[10]
    out += "\n\t\tFIN : "+ f[11]
    out += "\n\tWindows size : "+ str(int(tab.pop(0)+tab.pop(0),16))+" ("+tab.pop(0)+tab.pop(0)+")\n"
    out += "\tChecksum : "+ tab.pop(0)+tab.pop(0)+"\n"
    out += "\tUrgent Pointer : "+ tab.pop(0)+tab.pop(0)+"\n"
    optnumber = 1
    optTotalLength = headerLength -20
    while (optTotalLength > 0):
        out += "Option n° "+str(optnumber)+ "\n Type : "
        opt = tab.pop(0)
        if (opt == "00"): 
            out += "End of Options List\n"
            optTotalLength-=1
        elif (opt =="01"):
            out += "No Operation\n"
            optTotalLength-=1
        else:
            if (opt == "02"):
                out +="Maximum Segment Size \n"
            elif (opt == "03"):
                out +="WSOPT - Window Scale \n"
            elif (opt == "04"):
                out +="SACK Permitted \n"
            elif (opt == "05"):
                out +="SACK (Selective ACK) \n"
            elif (opt == "06"):
                out +="Echo (obsoleted by option 8) \n"
            elif (opt == "07"):
                out +="Echo Reply (obsoleted by option 8)  \n"
            elif (opt == "08"):
                out +="TSOPT - Time Stamp Option \n"
            elif (opt == "09"):
                out +="Partial Order Connection Permitted \n"
            elif (opt == "0a"):
                out +="Partial Order Service Profile \n"
            elif (opt == "0b"):
                out +="CC \n"
            elif (opt == "0c"):
                out +="CC.NEW \n"
            elif (opt == "0d"):
                out +="CC.ECHO \n"
            elif (opt == "0e"):
                out +="TCP Alternate Checksum Request \n"
            elif (opt == "0f"):
                out +="TCP Alternate Checksum Data \n"
            else:
                out += "Non Reconnu \n"
            optLength = tab.pop(0)
            optTotalLength -= int(optLength,16)
            out +="Length : " + str(int(optLength,16)) + " (0x"+optLength+")\n"
            out += "Option Data : "
            optLength = int(optLength,16)-2
            while(optLength > 1):
                #erreur out += tab.pop(0)
                optLength-=1
            out += "\n" 
        optnumber+=1
    out += "\tData : "+str(len(tab))+" octets \n"
    if (scrport == 80 or dstport == 80): out += http(tab)
    return out

def http(tab):
    out = "Couche http :\n"
    while (tab[0]!="20"): out += bytearray.fromhex(tab.pop(0)).decode()
    tab.pop(0)
    out +=" "
    while (tab[0]!="20"): out += bytearray.fromhex(tab.pop(0)).decode()
    tab.pop(0)
    out += " "
    while (tab[0]!="0d"): out += bytearray.fromhex(tab.pop(0)).decode()
    tab.pop(0)
    tab.pop(0)
    out += "\n"
    fin = 1
    while (fin) :
        cur = tab.pop(0)
        if (cur == "20"): out += " "
        elif (cur == "0d"): 
            if (prec == "0a"):
                fin =0
                out+="\n"
            out +="\n"
        else: out += bytearray.fromhex(tab.pop(0)).decode()
        prec = cur
    out += "\tData : "+" octets \n"
    return out

