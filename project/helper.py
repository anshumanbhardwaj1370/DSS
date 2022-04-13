import socket

host=('127.0.0.1', 56789)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(host)

c=0
clients = []
while True:

    data, address = sock.recvfrom(128)
    clients.append(address)
    data=data.decode()
    print(data)
    if (data=='ready'):
        c+=1
    if c==4:
        # sock.sendto(b'ready', address)
        break

for x in clients:
    print(x)
    sock.sendto(b'ready', x)
    # print
