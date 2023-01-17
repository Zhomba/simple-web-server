from socket import *

#Start test()
def test():

    #Specify the port
    serverPort = 80
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('',serverPort))

    serverSocket.listen(1)

    print("web server on port",serverPort)

    while True:

        #Establish the connection.
        print("ready to serve")

        #Create connection socket for accepted client.
        connectionSocket,addr = serverSocket.accept()

        try:

            message = connectionSocket.recv(1024)

            print(message)
            filename = message.split()[1]

            print(filename[1])

            print(filename,'||',filename[1])

            #Open the file
            f = open(filename[1:])
            outputdata = f.read()


            print(outputdata)

            #Send one HTTP header line into socket
            connectionSocket.send("""HTTP/1.0 200 OK
                        Content-Type: text/html

                    <html>
                    <head>
                    <title>Success</title>
                    </head>
                    <body>
                    Hello World!
                    </body>
                    </html>
                    """.encode());

            #connectionSocket.send(outputdata)

            #connectionSocket.send(message)
            connectionSocket.close()

        except IOError:

            #Send response message for the file not found.
            print ("404 Not Found")
            connectionSocket.send("""HTTP/1.0 404 Not Found\r\n""".encode());
            pass

        break
    pass

if __name__ =="__main__":
    test()
