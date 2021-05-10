import socket
import threading

HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECTED"


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client=socket.create_connection(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    print("1.",message)

    msg_length=len(message)
    print("2.",msg_length)

    send_length=str(msg_length).encode(FORMAT)
    print("3.",len(send_length))

    length=(HEADER -len(send_length))
    print("4.",length)

    send_length +=b' ' * length#b represents a byte here we are getting the byte of blank space " " here we are just padding
    print("5.",(send_length))

    client.send(send_length)
    client.send(message)
    print()

send("hello")
send("i am client2")
send(DISCONNECT_MESSAGE)

