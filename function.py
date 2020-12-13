def Ethernet(tab):
    out = "Destination address : "+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+"\n"
    out += "Source address : "+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+":"+tab.pop(0)+"\n"
    typeEternet = tab.pop(0)+tab.pop(0)
    if typeEternet == "0800":
        out += "EtherType = Ipv4 (0800)\n"
        out += Ipv4(tab)
    if typeEternet == "0806":
        out += "EtherType = ARP (0806)"
    return out


def Ipv4(tab):
    out = "Version : Ipv4 ("+ tab[0][0]+")\n"
    headerLength = int(tab[0][1],16)*4
    out += "Header Length : "+ str(headerLength) +" octets ("+tab.pop(0)[1]+")\n"
    out += "Type of Service :"+ tab.pop(0)+"\n" 
    t = int(tab[0]+tab[1],16)
    out += "Total Length : "+ str(t)+ " octets ("+ tab.pop(0)+tab.pop(0)+")\n"
    out += "Idientifier : 0x"+ tab.pop(0)+tab.pop(0)+ "\n"
    out += "Flags : "
    f = bin(int(tab.pop(0), 16))[2:].zfill(8)
    out += "\tReserved : "+ f[0]+"\n"
    out += "\tDon't Fragment (DF) : "+ f[1]+ "\n"
    out += "\tMore Fragment (MF) : "+f[2]+"\n"
    g = bin(int(tab.pop(0), 16))[2:].zfill(8)
    h = f[3:]+g
    out += "\tFragment Offset : "+ str(int(h,2))+"(0b"+str(h)+")\n"
    out += "Time to live (TTL) : "+str(int(tab[0],16))+"("+tab.pop(0)+")\n"
    proto = int(tab.pop(0),16)
    out += "Protocol : "
    if (proto == "01"): out += "ICMP (0x01)\n"
    elif (proto == "06"): print ("TCP (0x06)\n")
    elif (proto == "17"): out += "UDP (0x11)\n"
    else: out += "Non reconnu\n"
    out += "Header Checksum : "+ tab.pop(0)+tab.pop(0)+"\n"
    out += "Source Ip Adress : "+ str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"\n"
    out += "Destination Ip Adress : "+ str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"."+str(int(tab.pop(0),16))+"\n"
    #options

    return out

def tcp(tab):
    out = "Source port number : "+ str(int(tab.pop(0)+tab.pop(0),16))+"\n"
    out += "Destination port number : "+ str(int(tab.pop(0)+tab.pop(0),16))+"\n"
    out += "Sequence number : "+ tab.pop(0)+tab.pop(0)+tab.pop(0)+tab.pop(0)+"\n"
    out += "Acknowledgement number number : "+ tab.pop(0)+tab.pop(0)+tab.pop(0)+tab.pop(0)+"\n"
    headerLength = int(tab[0][1],16)*4
    out += "Header Length : "+ str(headerLength) +" octets ("+tab[0][0]+")\n"
    f = bin(int(tab.pop(0)[1]+tab.pop(0), 16))[2:].zfill(12)
    out += "Flags : \n"
    out += "\tNS : "+ f[3]
    out += "\n\tCWR : "+ f[4]
    out += "\n\tECE : "+ f[5]
    out += "\n\tURG : "+ f[6]
    out += "\n\tACK : "+ f[7]
    out += "\n\tPSH : "+ f[8]
    out += "\n\tRST : "+ f[9]
    out += "\n\tSYN : "+ f[10]
    out += "\n\tFIN : "+ f[11]
    out += "Windows size : "+ str(int(tab.pop(0)+tab.pop(0),16))+" ("+tab.pop(0)+tab.pop(0)+")\n"
    out += "Checksum : "+ tab.pop(0)+tab.pop(0)+"\n"
    out += "Urgent Pointer : "+ tab.pop(0)+tab.pop(0)+"\n"
    #options

    return out