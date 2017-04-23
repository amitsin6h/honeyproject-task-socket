import socket
import time


def client():
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

            #creating a socket object 
            server_socket = socket.socket()

            #connecting to host on port
            server_socket.connect((host,port))
        
            #get raw_input
            message = raw_input("Enter Your Message:")
            server_socket.send(message.encode())
                 
            server_socket.close()
 
client()
