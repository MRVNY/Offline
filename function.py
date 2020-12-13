def Ethernet(tab):
    print("Destination address : ",tab.pop(0),":",tab.pop(0),":",tab.pop(0),":",tab.pop(0),":",tab.pop(0),":",tab.pop(0),"\n")
    print("Source address : ",tab.pop(0),":",tab.pop(0),":",tab.pop(0),":",tab.pop(0),":",tab.pop(0),":",tab.pop(0),"\n")
    typeEternet = tab.pop(0)+tab.pop(0)
    if typeEternet == "0800":
        print("EtherType = Ipv4 (0806)\n")
        Ipv4(tab)
    if typeEternet == "0806":
        print("EtherType = ARP (0806)")


def Ipv4(tab):
    print("Version : Ipv4 (", tab[0][0],")\n")
    headerLength = int(tab[0][1],16)*4
    print("Header Length : ", headerLength ," octets (",tab.pop(0)[1],")\n")
    print("Type of Service :", tab.pop(0) )
    t = int(tab[0]+tab[1],16)
    print("Total Length : ", t, " octets (", tab.pop(0)+tab.pop(0),")\n")
    print("Idientifier : 0x", tab.pop(0)+tab.pop(0), "\n")
    print("Flags : ")
    f = bin(int(tab.pop(0), 16))[2:].zfill(8)
    print("\tReserved : ", f[0],"\n")
    print("\tDon't Fragment (DF) : ", f[1], "\n")
    print("\tMore Fragment (MF) : ",f[2],"\n")
    g = bin(int(tab.pop(0), 16))[2:].zfill(8)
    h = f[3:]+g
    print("\tFragment Offset : ", int(h,2),"(0b",h,")\n")
    print("Time to live (TTL) : ",int(tab[0],16),"(",tab.pop(0),")\n")
    proto = int(tab.pop(0),16)
    print("Protocol : ")
    if (proto == "01"): print("ICMP (0x01)\n")
    elif (proto == "06"): print ("TCP (0x06)\n")
    elif (proto == "17"): print("UDP (0x11)\n")
    else: print("Non reconnu\n")
    print("Header Checksum : ", tab.pop(0)+tab.pop(0),"\n")
    print("Source Ip Adress : ", int(tab.pop(0),16),".",int(tab.pop(0),16),".",int(tab.pop(0),16),".",int(tab.pop(0),16),"\n")
    print("Destination Ip Adress : ", int(tab.pop(0),16),".",int(tab.pop(0),16),".",int(tab.pop(0),16),".",int(tab.pop(0),16),"\n")
    #options

def tcp(tab):
    print("Source port number : ", int(tab.pop(0)+tab.pop(0),16),"\n")
    print("Destination port number : ", int(tab.pop(0)+tab.pop(0),16),"\n")
    print("Sequence number : ", int(tab.pop(0)+tab.pop(0)+tab.pop(0)+tab.pop(0)),"\n")
    print("Acknowledgement number number : ", int(tab.pop(0)+tab.pop(0)+tab.pop(0)+tab.pop(0)),"\n")
    headerLength = int(tab[0][1],16)*4
    print("Header Length : ", headerLength ," octets (",tab[0][0],")\n")
    f = bin(int(tab.pop(0)[1]+tab.pop(0), 16))[2:].zfill(12)
    print("Flags : \n")
    print("\tNS : ", f[3])
    print("\n\tCWR : ", f[4])
    print("\n\tECE : ", f[5])
    print("\n\tURG : ", f[6])
    print("\n\tACK : ", f[7])
    print("\n\tPSH : ", f[8])
    print("\n\tRST : ", f[9])
    print("\n\tSYN : ", f[10])
    print("\n\tFIN : ", f[11])
    print("Windows size : ", int(tab.pop(0)+tab.pop(0),16)," (",tab.pop(0)+tab.pop(0),")\n")
    print("Checksum : ", tab.pop(0)+tab.pop(0),"\n")
    print("Urgent Pointer : ", tab.pop(0)+tab.pop(0),"\n")
    #options