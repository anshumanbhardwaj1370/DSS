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
# print(sport)
dport=5060

host=('127.0.0.1', 56789)


sock1= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock1.bind(('127.0.0.1', port))
sock1.sendto(b'ready', host)

data1 = sock1.recv(1024).decode()
print(data1)
# if data !='ready':
#     print(data)

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
        # print(type(users))
    elif c<=(users+1):
        x=x[:-1]
        # print(x)
        words=x.split(" ")
        print(words[0],":",words[1])
        name_port[words[0]]=int(words[1])
        clients.append(int(words[1]))
        # print(clients)
    else:
        if x=="\n":
            break
            # print("yabba")
        x=x[:-1]
        # if (x)
        words=x.split(" ")
        sender=words[0]
        reciever=words[1]
        # if (sender==argv[1])
        # print(name_port[sender],"-->",name_port [reciever])

        if port==name_port [reciever]:
            # print(name_port [reciever])
            # def listen():
            # sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # sock2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # sock2.bind(('127.0.0.1', port))

                # while True:
                    # data = sock.recv(1024)
                    # print('\rpeer: {}\n> '.format(data.decode()), end='')
            # print(port)
            data2 = sock2.recv(1024)
            print(data2,"hehe")
            print('\r{}: {}\n> '.format(sender,data2.decode()), end='')
                # sock.close()

            # listener = threading.Thread(target=listen, daemon=True);
            # listener.start()

        elif port==name_port[sender]:
            # sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # sock3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # sock3.bind(('127.0.0.1', dport))

            # while True:
            # print(dport,"--->", name_port [reciever])
            # msg = input('> ')
            # words=x.split(" ")
            msg=""
            cc=1
            # print(words)
            for x in words:
                if cc>2:
                   msg+=x
                   msg+=" "
                cc+=1
            # print(msg)
            # print()
            sock3.sendto(msg.encode(), ('127.0.0.1', name_port [reciever]))
            # for x in clients:
            #     if x==name_port[reciever]:
            #         print(x)
            #         sock3.sendto(msg.encode(), ('127.0.0.1', x))
            #     # elif x==sport:
            #     #     # sock.sendto(b'ready', ('127.0.0.1', sport))
            #     #     # continue
            #     else:
            #         print(x,"aa")
            #         sock3.sendto(b'ready', ('127.0.0.1', x))

            # sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # sock4.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # sock4.bind(('127.0.0.1', port))
            # print(port)
            # data4 = sock4.recv(1024)
            # print(port,":",data4.decode())
            # print("done" ,msg)
            # sock.close()
        else:
            # sock5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # sock5.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # sock5.bind(('127.0.0.1', port))
            # data5 = sock5.recv(1024)
            # print(port,":",data5.decode())
            time.sleep(3)

        # print(x)
    c+=1
    time.sleep(2)
    # print(words)
    # print(x)
