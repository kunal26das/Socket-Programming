import socket

def Main():
    host = "127.0.0.1"
    port = 1001
                
    mySocket=socket.socket()
    mySocket.bind((host,port))
      
    mySocket.listen(1)
    print "\n Waiting for client..."
    conn, addr = mySocket.accept()
    print "\n Connection from : ",str(addr)

    while True:
        print "\n Waiting for response..."
        message = conn.recv(1024).decode()
        if message=="EXIT":
            print "\n Connection disconnected by client."
            break
        print " Message from client : ",message
        message = raw_input(str("\n Reply >> "))
        if message=="EXIT":
            conn.send(message.encode())
            break
        conn.send(message.encode())
                                                
    conn.close()
                
Main()
