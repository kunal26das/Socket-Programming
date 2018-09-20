import socket

def Main():
    host = '127.0.0.1'
    port = 1001
		
    mySocket = socket.socket()
    mySocket.connect((host,port))

    print "\n Connected to server."
	
    message = raw_input(str("\n Reply >> "))
		
    while True:
        mySocket.send(message.encode())
        print "\n Waiting for response..."
        message = mySocket.recv(1024).decode()
        if message=="EXIT":
            print "\n Connection disconnected by server."
            break
        print " Message from server :",message
        message = raw_input(str("\n Reply >> "))
        if message=="EXIT":
            mySocket.send(message.encode())
            break
	
    mySocket.close()

Main()
