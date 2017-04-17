import socket
 
def client():
        host = socket.gethostname()
        port =  2222

        #creating a socket object 
        server_socket = socket.socket()
       
       #connecting to host on port
        server_socket.connect((host,port))
        
        #get raw_input
        message = raw_input("Enter Your Message:")
        server_socket.send(message.encode())
                 
        server_socket.close()
 
client()
