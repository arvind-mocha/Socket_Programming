from socket import *

c=socket(AF_INET,SOCK_STREAM)

c.connect((gethostname(),999))

name=input("enter your name")
print("my name is",name)

c.send(bytes(name,'utf-8'))

msg=c.recv(1024).decode()

print(msg)
c.close()