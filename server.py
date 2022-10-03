# Index Number : 20000111
# Registration Number : 2020/CS/011
# Name : ANAWARATHNA M.A.D.V.S

import socket 

# in here client is work as a web browser
# server is work as a user computer


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET - IPv4 address family
# SOCK_STREAM - TCP socket
# these 2 variabels are default values to the socket function


print("Socket successfully created")

portNumber = 2728 # server port number 
host = '127.0.0.1'  # localhost(server host)

# bind the socket with between specific port number(2728) and host IP(localhost-127.0.0.1) address
# loclhost is a special IP address that accept any request
serverSocket.bind((host, portNumber))
print("Socket binded to %s" % (portNumber))


# start the server and frequncey(looping) finding the connection request from the client
serverSocket.listen(5) # 5 is the number of unaccepted connections that the system will allow before binding the new connections
print("Now Socket is listening") 



# this loop is work infinity to accept the connection request from the client(web browser)
# and send the message to the client
# afetr send then close the connection
# and then again wait for the next connection request from the client 
# likewise this loop is work until the server is shutdown by the user(server owner - we)

while True:  # loop to find the connection request from the client
    
    connection, address = serverSocket.accept() # accept the connection request from the client
    print('Got connection from', str(address)) # print the gotted client address on the console

    request = connection.recv(1024).decode('utf-8') 
    # recive the request from the client and it decode using utf-8 encoding system
    
    # print(request) # print the requested informations on the console, it is as follows

    # GET / HTTP/1.1
    # Host: localhost:2728
    # Connection: keep-alive
    # sec-ch-ua: "Not-A.Brand";v="99", "Opera";v="91", "Chromium";v="105"
    # sec-ch-ua-mobile: ?0
    # sec-ch-ua-platform: "Windows"
    # and some other header information......
    

    header = request.split(' ') # split the same request from the white space and store in the header array
    
    # print(header) # print the header on the console, it is as follows
    
    # ['GET', '/', 'HTTP/1.1\r\nHost:', 'localhost:2728\r\nConnection:', 'keep-alive\r\nsec-ch-ua:', '"Not-A.Brand";v="99",', '"Opera";v="91",', '"Chromium";v="105"\r\nsec-ch-ua-mobile:', '?0\r\nUser-Agent:', 'Mozilla/5.0', '(Windows', 'NT', '10.0;', 'Win64;', 'x64)', 'AppleWebKit/537.36', '(KHTML,', 'like', 'Gecko)', 'Chrome/105.0.0.0', 'Safari/537.36', 'OPR/91.0.4516.20\r\nsec-ch-ua-platform:', '"Windows"\r\nAccept:', 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8\r\nSec-Fetch-Site:', 'same-origin\r\nSec-Fetch-Mode:', 'no-cors\r\nSec-Fetch-Dest:', 'image\r\nReferer:', 'http://localhost:2728/\r\nAccept-Encoding:', 'gzip,', 'deflate,', 'br\r\nAccept-Language:', 'en-US,en;q=0.9\r\n\r\n']
    
    # header[1] - This is the requested file path from the client(web browser)
    
    try:
        currentPath = header[1] # get the requested path from client(web browser url)
    except IndexError:
        currentPath = '/' # if the header list index is out of the index then set the path to the root path

    
    print("Current Path :" + currentPath) # print the current path on the console
    

    if currentPath == '/' : 
        # if the path is root path(/-localhost or default route) then send the index.html file content to the client => http://localhost:2728 or  http://localhost:2728/
        currentPath = './htdocs/index.html' # set the current path to the index.html file
        print("Connected to index.html") 
        

    elif currentPath == '/aboutme' or currentPath == '/aboutme.html': # if the path is aboutme path(/aboutme) then send the aboutme.html file content to the client => http://localhost:2728/aboutme
        currentPath = './htdocs/aboutMe.html' # set the current path to the aboutMe.html file
        print("Connected to aboutMe.html") 
        
    try:
        file = open(currentPath) # open the file and file path is taken as a currentPath (./htdocs/index.html or ./htdocs/aboutMe.html)
        fileContent = file.read() # read the file content
        file.close() # close the file

        response = 'HTTP/1.x 200 OK\n\n' + fileContent # create the response with the file content 
        
        # HTTP - protocol
        # 1.x - version
        # 200 - status code(successful response status code)
        # OK - status message
        # fileContent - file content of that the above opened file 
        
        
    except:
        response = 'HTTP/1.x 404 Not Found\n\nPage is not Found - Error Deteted 404' # if the file is not found then sent the response to the client with the error message
        print("Page is not Found - Error Deteted 404") # print the error message on the console
    
    connection.sendall(response.encode()) # send the response to the client with uncoded response 
    connection.close() # close the connection


serverSocket.close() # close the server socket
