import socket
import time


def server():
    localtime = time.asctime(time.localtime(time.time()))
    try:
        logs = open("logs.txt","a")
        config_file = open("config.txt","r")
        data = {}
        for file_data in config_file:
            k, v = file_data.strip().split('=')
            data[k.strip()] = v.strip()
        port_no = int(data['port'])
    except IOError:
        logs.write("%s IOError: can\'t find file or read data \n" % ([localtime]))
        logs.close()
    except KeyError:
        logs.write("%s KeyError: key not found on dictionary \n" % ([localtime]))
    else:
        host = socket.gethostname()
        port = port_no   
    
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
