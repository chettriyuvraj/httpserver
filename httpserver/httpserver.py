import socket 
#importing from helpers.py in same directory
import helpers
from helpers import parse_filename as parse_filename
from helpers import check_file_exists as check_file_exists
from helpers import read_html_file as read_html_file

HOST, PORT = '0.0.0.0',50009    #0.0.0.0 - listening to all incoming connections and setting port as 50008
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a server-side socket 
server_socket.bind((HOST,PORT)) #binding the socket 

print("Socket bound..")
print(f"Port - {PORT} \n")

with server_socket as s: 
    s.listen(5)          # listening for connects
    print("Now waiting for requests")
    conn,address = s.accept()       #accepting connection from client 
    with conn: 
        #print('Received by',address)
        while True:
            header_data = conn.recv(1024) #value - header data received as bytes 
                
            file_name = parse_filename(header_data) #let's parse filename from header_request
            
            status_code='' #status code for http response 
            response_string = '' #server sends the response html file content as a string 
            response_data='' #response in http format

            
            if check_file_exists(file_name) == True:
                status_code = '200' #status code 200 means request accepted file is being served
                response_string = read_html_file(file_name) #the file to be served in string format
                response_data = f'HTTP/1.1 {status_code} OK\nContent-Type: text/html\nContent-Length: {len(response_string)}\n\n{response_string}'  
                
            else:
                status_code = '404'  #file not found
                response_string = 'Error 404! No such file exists.'
                response_data = f'HTTP/1.1 {status_code} OK\nContent-Type: text/plain\nContent-Length: {len(response_string)}\n\n{response_string}'
            
            response_data = response_data.encode() #converting response data from string to bytes
            
            conn.sendall(response_data) #send response to client
            
            print("The request from the client is \n\n")
            print(header_data) #prints the http request from the client each time to show that client is indeed sending request
            print('\n\n')
            
    
