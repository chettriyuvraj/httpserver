import os
import os.path
from os import path
import codecs

def parse_filename(header_data): #function to parse the filename requested by the HTTP request - from the HTTP request
    str_header_data = str(header_data) #the http request is in bytes - converting it to string
    file_name='' 
    current_char='/' 
    index = 7                        #filename always happens to starts from 7th char so we will parse character by character from there
    while(current_char!=' '):        #parsing character by character until blank encountered
        current_char=str_header_data[index]
        file_name+=current_char      #each character appended to filename
        index+=1
    file_name=file_name.replace(" ","")    #filename has a space at the end, removing it
    return os.path.normpath(file_name)     #removing any other discrepancies that might have crept in

def check_file_exists(file_name):     #function to check if file requested exists in the current directory 
   
    from os import path
    return path.exists(file_name)     #function of the os module 

def read_html_file(file_name):        #function to read html file 
    
    f=codecs.open(file_name,'r')
    return f.read()