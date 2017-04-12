import socket
 
def Main():
    host = "127.0.0.1"
    port = 5000
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
    print "------------------------------------------"
    print "-------------------------------------------"
    print "Server Sucessfully Started!!"
    print "Socket binded to %s" %(port)
     
    mySocket.listen(1)
    print "Socket is listening"
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))

    data = conn.recv(1024).decode()
    print ("Received Message: " + str(data))
             
             
    conn.close()
     
if __name__ == '__main__':
    Main()
