import socket
import sys
import threading
import time

file1 = open("input.txt","r+") 
lines=file1.readlines()

name_port={}
users = 0

clients=[]

port=int(sys.argv[1])
dport=5060

host=('127.0.0.1', 56789)


sock1= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock1.bind(('127.0.0.1', port))
sock1.sendto(b'ready', host)

data1 = sock1.recv(1024).decode()
print(data1)


sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock2.bind(('127.0.0.1', port))

sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock3.bind(('127.0.0.1', dport))


c=1
for x in lines:
    if c==1:
        users=int(x[0])
        
    elif c<=(users+1):
        x=x[:-1]
        
        words=x.split(" ")
        print(words[0],":",words[1])
        name_port[words[0]]=int(words[1])
        clients.append(int(words[1]))
    else:
        if x=="\n":
            break
            
        x=x[:-1]
        
        words=x.split(" ")
        sender=words[0]
        reciever=words[1]

        if port==name_port [reciever]:
            
            data2 = sock2.recv(1024)
            # print(data2,"hehe")
            print('\r{}: {}\n> '.format(sender,data2.decode()), end='')
                

        elif port==name_port[sender]:
            #
            msg=""
            cc=1
            
            for x in words:
                if cc>2:
                   msg+=x
                   msg+=" "
                cc+=1
           
            sock3.sendto(msg.encode(), ('127.0.0.1', name_port [reciever]))
            #
        else:
            time.sleep(3)

    c+=1
    # time.sleep(2)
