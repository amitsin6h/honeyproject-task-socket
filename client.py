import socket
 
def Main():
        host = '127.0.0.1'
        port = 5000
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        print "------------------------------------"
        print "------------------------------------"
        message = raw_input("Enter Your Message:")
        mySocket.send(message.encode())
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
