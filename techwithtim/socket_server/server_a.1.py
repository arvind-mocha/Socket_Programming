from socket import *
print("my host name is",gethostname())#prints the host name which is desktop name

s=socket(AF_INET,SOCK_STREAM)#it is not a problem even if you dont pass parameter here but it os always good to mention
                             #by default if you dont give parameters it is a v4 address family and TCP connection
                             #AF_INET = it metions that your ip address belongs to v4family there is also
                             #AF_INET6 which metions ip address belongs to the family v6
                             #SOCK_STREAM tells that it is a TCP connection
                             #SOCK_DGRAM tells that it is a UDP connection
print("socket created")



s.bind((gethostname(),999))#bind accepts only one parameter so two parameters are passed as one by (())
                            #bind is bassically present in server not client because client job is only
                            #to connect with the server but server job is to create a portal for connections



s.listen(5)#since we pass 5 only 5 client can wait for server more than that is blocked
print("waiting for connection")

while True:#this loop is to get continuous stream message from the client without interruption

    c,addr=s.accept()   #c indicates the client and addr indicates the client address

    name=c.recv(1024).decode()#since client sends bytes we need o decode it

    print("connected with",addr,"belongs to",name)

    c.send(bytes("welcome to server",'utf-8'))#so we send it in bytes bytes method which converts string into bytes
                                              #utf - unicode transformation format 8 describs 8 bit we can also us
                                              #utf-16,utf-32 it encodes the msg which is decoded in client side
                                              #sending to client msg no.1


s.close()