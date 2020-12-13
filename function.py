def Ethernet(tab):
    out = "Couche Eternet : \n"
    out += "\tDestination address : "+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+"\n"
    out += "\tSource address : "+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+"\n"
    typeEternet = tab.pop(0)+tab.pop(0)
    if typeEternet == "0800":
        out += "\tEtherType : Ipv4 (0x0800)\n"
        out += "\tData : "+str(len(tab))+" octets \n"
        out += Ipv4(tab)
    if typeEternet == "0806":
        out += "\tEtherType : ARP (0x0806)\n"
    return out


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
    if (proto == 1): out += "\tICMP (0x01)\n"
    elif (proto == 6): out += ("\tTCP (0x06)\n")
    elif (proto == 17): out += "\tUDP (0x11)\n"
    else: out += "\tNon reconnu\n"
    out += "\tHeader Checksum : 0x"+ tab.pop(0)+tab.pop(0)+"\n"
    out += "\tSource Ip Adress : "+ str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"\n"
    out += "\tDestination Ip Adress : "+ str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"\n"
    #options
    out += "\tData : "+str(len(tab))+" octets \n"
    if (proto ==6): out+= tcp(tab)
    return out

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
    #options
    out += "\tData : "+str(len(tab))+" octets \n"
    if (scrport == 80 | dstport == 80): out+= http(tab)
    return out

def http(tab):
    out = "Couche http :\n"
    while (tab[0]!="20"): out += chr(tab.pop(0))
    tab.pop(0)
    out +=" "
    while (tab[0]!="20"): out += chr(tab.pop(0))
    tab.pop(0)
    out += " "
    while (tab[0]!="0d"): out += chr(tab.pop(0))
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
        else: out += chr(tab.pop)
        prec = cur
    out += "\tData : "+" octets \n"
    return out

