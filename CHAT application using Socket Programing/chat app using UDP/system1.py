import socket
import os
import threading

#send
client1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sIP = "192.168.1.5"
sPORT = 8881
def send():
    while True:
        data=input("")
        if(data=="exit"):
            break
        print("msg sent---> ",data)
        client1.sendto(data.encode(),(sIP,sPORT))
	
        
        
#recived
client2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip="192.168.1.7"
port=8887
client2.bind((ip,port))
def recv():
    while True:
        x=client2.recvfrom(1024)
        if(x[0].decode()=='exit'):
            print("End")
            break
        print("recived---> ",x[0].decode())

t2 = threading.Thread(target=recv)
t1 = threading.Thread(target=send)

t2.start()
t1.start()
