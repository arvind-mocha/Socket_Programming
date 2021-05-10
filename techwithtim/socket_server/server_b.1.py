import socket
import threading
import time



HEADER=64       #64 bytes
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
FORMAT='utf-8' #even it can be 'ascii'
DISCONNECT_MESSAGE="!DISCONNECTED"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn,addr):
    print(f"NEW CONNECTION {addr} is connected")

    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)#HEADER is 64 bytes FORMAT is 'utf-8' since we dont know the size of recieving bit we do this
        if msg_length:
            msg_length=int(msg_length)#so the recieved message is converted into integer to get the size
            msg=conn.recv(msg_length).decode(FORMAT)#now the correct size of the msg is passed
            if msg==DISCONNECT_MESSAGE:
                connected=False
            print(f"[{addr}],{msg}")
            conn.send("message recieved".encode(FORMAT))
            conn.send(msg.encode(FORMAT))

    conn.close()



def start():
    server.listen()
    print(f"[LISTNING] server is listening on {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))#here we are telling where to pass the parameter using target and what is to be passed using args
                                                                      #while True a thread is created and arguments are passed i we disconnect the thread no new thread is created

        time.sleep(2)
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")#there is a string called f string represented by f"" which takes takes things inside {}
                                                                   # this as expression where the value of the expression is printed.here we take the no of thread as the no
                                                                   # of client and we reduce 1 withit since start thread runs always tlisten




print("[SERVER GETTING LOADED].........")
start()




