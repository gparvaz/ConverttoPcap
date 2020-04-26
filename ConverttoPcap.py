
import os
import sys
import random 

frame_filename='C:/Users/admin/Desktop/ForTest/Compressed_By_Deflate.binary'

f=open(frame_filename,'rb')
tdata = f.read()
f.close()


packetsize=os.path.getsize(frame_filename)
packetsize
  
datalinkNo=155;
lenlittleEndianP2=int(packetsize/256)
lenlittleEndianP1=packetsize-(lenlittleEndianP2*256)


pcap_file=[0xD4,0xC3,0xB2,0xA1,0x02,0x00,0x04,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x04,0x00,datalinkNo,0x00,0x00,0x00]
packetHeader= [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,lenlittleEndianP1,lenlittleEndianP2,0x00,0x00,lenlittleEndianP1,lenlittleEndianP2,0x00,0x00] 


globalHeader = bytearray(pcap_file)
PacKlHeader = bytearray(packetHeader)
packet=bytearray(tdata)


for j in range(0,16):
    globalHeader.append(PacKlHeader[j])
    


j=0
while j < packetsize:  
    globalHeader.append(packet[j])
    j=j+1


finalpcapname=""
d=random.randrange(1, 100)

fname = ['Final_OutPut', str(d) ,'.pcap']
finalpcapname = finalpcapname.join(fname)
fw = open(finalpcapname,'wb')
fw.write(globalHeader)
fw.close()
print(finalpcapname)
    
    