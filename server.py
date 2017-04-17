import socket
 
def server():
    host = socket.gethostname()
    port = 2222
    
    #creating socket object
    server_socket = socket.socket()
   
   #bindig host and port
    server_socket.bind((host,port))
    
    #response up to 3 request    
    server_socket.listen(3)
   
    client_socket, addr = server_socket.accept()
    print ("Got connection from: " + str(addr))

    data = client_socket.recv(1024).decode()
    print ("Received message: " + str(data))
             
             
    client_socket.close()
     
server()
