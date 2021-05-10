import socket


HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECTED"


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client=socket.create_connection(ADDR)

def send(msg):
    message=msg.encode(FORMAT)#byte value of string is b'value'
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length +=b' ' * (HEADER -len(send_length))#we are converting int into byte because we cant use encode as int does not support encode
    client.send(send_length)
    client.send(message)
    msg1=client.recv(2048).decode(FORMAT)
    msg2=client.recv(2048).decode(FORMAT)
    print(msg1)
send("hello")
input()
send("i am client1")
input()
send(DISCONNECT_MESSAGE)
