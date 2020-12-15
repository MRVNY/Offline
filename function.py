def Ethernet(tab):
    title = "Ethernet"
    t = len(tab)
    out = "Couche Ethernet : \n"
    out += "\tDestination address : "+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+"\n"
    out += "\tSource address : "+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+"\n"
    typeEternet = tab.pop(0)+tab.pop(0)
    if typeEternet == "0800":
        out += "\tEtherType : 0x0800 (IPv4)\n"
        out += "\tData : "+str(len(tab))+" octets \n"
        if(len(tab) != t-14) : raise Exception("Erreur traitement")
        s,title = Ipv4(tab)
        out += s
    elif typeEternet == "0806":
        out += "\tEtherType : 0x0806 (ARP)\n"
        out += "\tData : "+str(len(tab))+" octets \n"
        if(len(tab) != t-14) : raise Exception("Erreur traitement")
    else : 
        out += "\tEtherType : 0x"+typeEternet+" (Non reconnu)\n"
        out += "\tData : "+str(len(tab))+" octets \n"
        if(len(tab) != t-14) : raise Exception("Erreur traitement")
    return out,title


def Ipv4(tab):
    out = "\nCouche Ip :\n"
    out += "\tVersion : 0x"+ tab[0][0]+" (Ipv4)\n"
    headerLength = int(tab[0][1],16)*4
    out += "\tHeader Length : 0x"+tab.pop(0)[1]+" ("+str(headerLength) +" octets)\n"
    out += "\tType of Service : 0x"+ tab.pop(0) +"\n"
    t = int(tab[0]+tab[1],16)
    out += "\tTotal Length : 0x"+ tab.pop(0)+tab.pop(0)+" ("+str(t)+ " octets )\n"
    out += "\tIdentifier : 0x"+ tab.pop(0)+tab.pop(0)+ "\n"
    out += "\tFlags : "
    f = bin(int(tab.pop(0), 16))[2:].zfill(8)
    out += "\tReserved : "+ f[0]+"\n"
    out += "\t\tDon't Fragment (DF) : "+ f[1]+ "\n"
    out += "\t\tMore Fragment (MF) : "+f[2]+"\n"
    g = bin(int(tab.pop(0), 16))[2:].zfill(8)
    h = f[3:]+g
    out += "\t\tFragment Offset : "+ str(int(h,2))+"(0b"+str(h)+")\n"
    out += "\tTime to live (TTL) : 0x"+tab.pop(0)+" ("+str(int(tab[0],16))+")\n"
    proto = int(tab.pop(0),16)
    out += "\tProtocol : "
    if (proto == 1): 
        out += "\t0x01 (ICMP)\n"
        protoname = "ICMP"
    elif (proto == 6): 
        out += ("\t0x06 (TCP)\n")
        protoname = "TCP"
    elif (proto == 17): 
        out += "\t0x11 (UDP)\n"
        protoname = "UDP"
    else: 
        out += "\tNon reconnu\n"
        protoname = "Unknown"
    out += "\tHeader Checksum : 0x"+ tab.pop(0)+tab.pop(0)+"\n"
    ipsrc = str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))
    out += "\tSource Ip Adress : "+ipsrc+"\n"
    ipdst = str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))
    out += "\tDestination Ip Adress : "+ipdst+"\n"
    #option
    optnumber = 1
    optTotalLength = headerLength -20
    while (optTotalLength > 0):
        out += "Option n° "+str(optnumber)+ "\n Type : "
        opt = tab.pop(0)
        if (opt == "00"): 
            out += "0x00 (End of Options List)\n"
            optTotalLength-=1
        elif (opt =="01"):
            out += "0x01 (No Operation)\n"
            optTotalLength-=1
        elif (opt == "07"):
            out += "0x07 (Record Route)\n"
            optLength = tab.pop(0)
            optTotalLength -=int(optLength,16)
            out += "Length : " + str(int(optLength,16)) +" (Ox"+ str(optLength)+ ")\n"
            out += "Pointer : 0x"+ tab.pop(0)+"\n"
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
    if(len(tab) != t-headerLength) : raise Exception("Erreur traitement")
    if (proto ==6): 
        s,protoname = tcp(tab)
        out += s
    title = "Src: "+ipsrc.ljust(15,' ')+"\tDst: "+ipdst.ljust(15, ' ')+"\tProtocol: "+protoname
    return out,title

def tcp(tab):
    t = len(tab)
    protoname = "TCP"
    out = "\nCouche tcp \n"
    scrport = int(tab.pop(0)+tab.pop(0),16)
    out += "\tSource port number : "+ str(scrport)+"\n"
    dstport = int(tab.pop(0)+tab.pop(0),16)
    out += "\tDestination port number : "+ str(dstport)+"\n"
    out += "\tSequence number : 0x"+ tab.pop(0)+tab.pop(0)+tab.pop(0)+tab.pop(0)+"\n"
    out += "\tAcknowledgement number : 0x"+ tab.pop(0)+tab.pop(0)+tab.pop(0)+tab.pop(0)+"\n"
    headerLength = int(tab[0][0],16)*4
    out += "\tHeader Length : "+ str(headerLength) +" octets (0x"+tab[0][0]+")\n"
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
    windSize = tab.pop(0)+tab.pop(0)
    out += "\n\tWindows size : "+ str(int(windSize,16))+" (0x"+windSize+")\n"
    out += "\tChecksum : 0x"+ tab.pop(0)+tab.pop(0)+"\n"
    out += "\tUrgent Pointer : 0x"+ tab.pop(0)+tab.pop(0)+"\n"
    optnumber = 1
    optTotalLength = headerLength -20
    while (optTotalLength > 0):
        out += "\tOption n° "+str(optnumber)+ "\n \t\tType : "
        opt = tab.pop(0)
        if (opt == "00"): 
            out += "0x00 (End of Options List)\n"
            optTotalLength-=1
        elif (opt =="01"):
            out += "0x01 (No Operation)\n"
            optTotalLength-=1
        else:
            if (opt == "02"):
                out +="0x02 (Maximum Segment Size) \n"
            elif (opt == "03"):
                out +="0x03 (WSOPT - Window Scale) \n"
            elif (opt == "04"):
                out +="0x04 (SACK Permitted) \n"
            elif (opt == "05"):
                out +="0x05 (SACK (Selective ACK)) \n"
            elif (opt == "06"):
                out +="0x06 (Echo (obsoleted by option 8)) \n"
            elif (opt == "07"):
                out +="0x07 (Echo Reply (obsoleted by option 8))  \n"
            elif (opt == "08"):
                out +="0x08 (TSOPT - Time Stamp Option) \n"
            elif (opt == "09"):
                out +="0x09 (Partial Order Connection Permitted) \n"
            elif (opt == "0a"):
                out +="0x0a (Partial Order Service Profile) \n"
            elif (opt == "0b"):
                out +="0x0b (CC) \n"
            elif (opt == "0c"):
                out +="0x0c (CC.NEW) \n"
            elif (opt == "0d"):
                out +="0x0d (CC.ECHO) \n"
            elif (opt == "0e"):
                out +="0x0e (TCP Alternate Checksum Request) \n"
            elif (opt == "0f"):
                out +="0x0f (TCP Alternate Checksum Data) \n"
            else:
                out += "0x"+opt+ " (Non Reconnu) \n"
            optLength = tab.pop(0)
            optTotalLength -= int(optLength,16)
            out +="\t\tLength : " + str(int(optLength,16)) + " (0x"+optLength+")\n" 
            optLength = int(optLength,16)-2
            if (optLength > 0) : 
                out += "\t\tOption Data : "
                out +="0x"
            while(optLength > 0):
                out += tab.pop(0)
                optLength-=1
            out += "\n" 
        optnumber+=1
    out += "\tData : "+str(len(tab))+" octets \n"
    if(len(tab) != t-headerLength) : raise Exception("Erreur traitement")
    if (scrport == 80 or dstport == 80): 
        tmp = ""
        if(len(tab)>20):
            for i in range(20): tmp += bytearray.fromhex(tab[i]).decode()
            if('HTTP' in tmp): 
                out += http(tab)
                protoname = 'HTTP'
    return out, protoname

def http(tab):
    out = "\nCouche http :\n\t"
    while (tab[0]!="0d"): out += bytearray.fromhex(tab.pop(0)).decode()
    tab.pop(0)
    tab.pop(0)
    out += "\n\t"
    fin = 1
    while (fin) :
        cur = tab.pop(0)
        if (cur == "0d"): 
            if (prec == "0a"):
                tab.pop(0)
                fin =0  
        else: out += bytearray.fromhex(cur).decode()
        if (bytearray.fromhex(cur).decode() == "\n") : out += "\t"
        prec = cur
    
    out += "Data : "+str(len(tab))+" octets \n"
    return out

