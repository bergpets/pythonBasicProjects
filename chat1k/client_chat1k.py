import socket
print('type "exit" to exit')
clientname = input('enter your nickname:')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 2222))

flag = True
while flag:
    client.send(input(clientname, ': ').encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        flag = False
    else:
        print(msg)
        
client.close()