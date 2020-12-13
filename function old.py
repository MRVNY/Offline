def Ethernet(tab, p:int):
    print("Destination address : ",tab[p],":",tab[p+1],":",tab[p+2],":",tab[p+3],":",tab[p+4],":",tab[p+5],"\n")
    p+=6
    print("Source address : ",tab[p],":",tab[p+1],":",tab[p+2],":",tab[p+3],":",tab[p+4],":",tab[p+5],"\n")
    p+=6
    typeEternet = tab[p]+tab[p+1]
    p+=2
    if typeEternet == "0800":
        print("EtherType = Ipv4 (0806)\n")
        Ipv4(tab,p)
    if typeEternet == "0806":
        print("EtherType = ARP (0806)")


def Ipv4(tab, p:int):
    print("Version : Ipv4 (", tab[p][0],")\n")
    headerLength = int(tab[p][1],16)*4
    print("Header Length : ", headerLength ," octets (",tab[p][1],")\n")
    p+=1
    print("Type of Service :", tab[p] )
    p+=1
    t = int(tab[p]+tab[p+1],16)
    print("Total Lenght : ", t, " octets (", tab[p]+tab[p+1],")\n")
    p=+2
    print("Idientifier : 0x", tab[p]+tab[p+1], "\n")
    p=+2
    print("Flags : ")
    f = bin(int(tab[p], 16))[2:].zfill(8)
    print("\tReserved : ", f[0],"\n")
    print("\tDon't Fragment (DF) : ", f[1], "\n")
    print("\tMore Fragment (MF) : ",f[2],"\n")
    g = bin(int(tab[p+1], 16))[2:].zfill(8)
    h = f[3:]+g
    print("\tFragment Offset : ", int(h,2),"(0b",h,")\n")
    p+=2
    print("Time to live (TTL) : ",int(tab[p],16),"(",tab[p],")\n")
    p+=1
    proto = int(tab[p],16)
    print("Protocol : ")
    if (proto == "01"): print("ICMP (0x01)\n")
    elif (proto == "06"): print ("TCP (0x06)\n")
    elif (proto == "17"): print("UDP (0x11)\n")
    else: print("Non reconnu\n")
    p+=1
    print("Header Checksum : ", tab[p]+tab[p+1],"\n")
    p+=2
    print("Source Ip Adress : ", int(tab[p],16),".",int(tab[p+1],16),".",int(tab[p+2],16),".",int(tab[p+3],16),"\n")
    p+=4
    print("Destination Ip Adress : ", int(tab[p],16),".",int(tab[p+1],16),".",int(tab[p+2],16),".",int(tab[p+3],16),"\n")
    p+=4
    #options

def tcp(tab,p:int):
    print("Source port number : ", int(tab[p]+tab[p+1],16),"\n")
    p+=2
    print("Destination port number : ", int(tab[p]+tab[p+1],16),"\n")
    p+=2
    print("Sequence number : ", int(tab[p]+tab[p+1]+tab[p+2]+tab[p+3]),"\n")
    p+=4
    print("Acknowledgement number number : ", int(tab[p]+tab[p+1]+tab[p+2]+tab[p+3]),"\n")
    p+=4
    headerLength = int(tab[p][1],16)*4
    print("Header Length : ", headerLength ," octets (",tab[p][0],")\n")
    f = bin(int(tab[p][1]+tab[p+1], 16))[2:].zfill(12)
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
    p+=2
    print("Windows size : ", int(tab[p]+tab[p+1],16)," (",tab[p]+tab[p+1],")\n")
    p+=2
    print("Checksum : ", tab[p]+tab[p+1],"\n")
    p+=2
    print("Urgent Pointer : ", tab[p]+tab[p+1],"\n")
    p+=2
    #options